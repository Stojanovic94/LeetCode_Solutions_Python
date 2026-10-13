import numpy as np

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # n = len(nums)
        # nums = sorted(map(abs, nums))
        # return sum(x * x for x in nums[n//2:]) - sum(x * x for x in nums[:n//2])

        sq = np.square(np.array(nums, dtype=np.int64))
        h = len(nums) // 2
        return int(sq.sum() - 2 * np.partition(sq, h)[:h].sum())  # smallest h squares moved to the front, O(n)
    