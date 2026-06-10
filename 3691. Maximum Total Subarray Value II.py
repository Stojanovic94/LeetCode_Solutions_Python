import heapq
from itertools import count as uid_counter

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n   = len(nums)
        vis = set()

        # Sort indices by value (ascending), ties broken by index
        ids = sorted(range(n), key=lambda x: (nums[x], x))

        uid = uid_counter()   # tie-breaker for the heap

        def compute_val(i, j, l, r):
            """
            Find the max-spread pair within position window (i, j) exclusive,
            searching within ids[l..r].
            Returns (val, i, j, l, r) or None if invalid / already visited.
            """
            if (i, j) in vis:
                return None
            vis.add((i, j))

            # Advance l until ids[l] is strictly inside (i, j)
            while l < n and (ids[l] <= i or ids[l] >= j):
                l += 1
            # Retreat r until ids[r] is strictly inside (i, j)
            while r >= 0 and (ids[r] <= i or ids[r] >= j):
                r -= 1

            if l > r:
                return None

            val = nums[ids[r]] - nums[ids[l]]
            return (val, i, j, l, r) if val > 0 else None

        res = 0
        pq  = []   # max-heap (negate val)

        first = compute_val(-1, n, 0, n - 1)
        if first:
            val, i, j, l, r = first
            heapq.heappush(pq, (-val, next(uid), i, j, l, r))

        while pq and k > 0:
            neg_val, _, i, j, l, r = heapq.heappop(pq)
            val = -neg_val

            # Positions of the min-value and max-value elements
            ni = min(ids[l], ids[r])   # leftmost of the two extreme positions
            nj = max(ids[l], ids[r])   # rightmost

            # Number of (left, right) pairs with left in (i, ni] and right in [nj, j)
            cnt  = min((ni - i) * (j - nj), k)
            k   -= cnt
            res += val * cnt

            # Split into two sub-problems and push their best pairs
            for entry in [compute_val(ni, j, l, r),
                          compute_val(i, nj, l, r)]:
                if entry:
                    ev, ei, ej, el, er = entry
                    heapq.heappush(pq, (-ev, next(uid), ei, ej, el, er))

        return res