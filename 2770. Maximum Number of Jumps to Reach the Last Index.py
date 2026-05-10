from bisect import bisect_left, bisect_right

class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [-1] * (4 * size)

    def update(self, idx, val, node, start, end):
        if start == end:
            self.tree[node] = max(self.tree[node], val)
            return
        
        mid = (start + end) // 2
        if idx <= mid:
            self.update(idx, val, 2 * node, start, mid)
        else:
            self.update(idx, val, 2 * node + 1, mid + 1, end)
        
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, l, r, node, start, end):
        if r < start or end < l:
            return -1
        
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left = self.query(l, r, 2 * node, start, mid)
        right = self.query(l, r, 2 * node + 1, mid + 1, end)
        return max(left, right)


class Solution:
    def maximumJumps(self, nums, target):
        n = len(nums)

        # ✅ Step 1: Coordinate Compression
        sorted_vals = sorted(set(nums))
        
        def get_index(x):
            return bisect_left(sorted_vals, x)

        st = SegmentTree(len(sorted_vals))
        
        dp = [-1] * n
        dp[-1] = 0

        # Update last element
        idx = get_index(nums[-1])
        st.update(idx, 0, 1, 0, len(sorted_vals) - 1)

        # ✅ Step 2: Process from right → left
        for i in range(n - 2, -1, -1):
            left_val = nums[i] - target
            right_val = nums[i] + target

            # Find range in compressed indices
            l = bisect_left(sorted_vals, left_val)
            r = bisect_right(sorted_vals, right_val) - 1

            if l <= r:
                best = st.query(l, r, 1, 0, len(sorted_vals) - 1)
                if best != -1:
                    dp[i] = 1 + best

            # Update segment tree
            idx = get_index(nums[i])
            if dp[i] != -1:
                st.update(idx, dp[i], 1, 0, len(sorted_vals) - 1)

        return dp[0]