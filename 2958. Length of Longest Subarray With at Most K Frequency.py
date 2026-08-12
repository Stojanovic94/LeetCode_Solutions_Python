class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        from collections import deque
        max_len = 0
        counts = dict()
        dq = deque()
        for num in nums:
            val = counts.get(num, 0)
            if(val < k):
                counts[num] = val + 1
                dq.append(num)
                max_len = max(max_len, len(dq))
                continue
            else:
                while(dq[0] != num):
                    counts[dq.popleft()] -= 1
                dq.popleft()
                dq.append(num)
                counts[num] = k
                max_len = max(max_len, len(dq))
        return max_len