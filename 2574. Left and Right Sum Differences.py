class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        arr = []
        for i,cur_val in enumerate(nums):
            arr.append(abs(total_sum - left_sum - cur_val))
            left_sum += cur_val
            total_sum -= cur_val
        return arr