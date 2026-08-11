class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        index = 1
        while index < len(nums) and nums[index] == nums[index - 1] + 1:
            prefix_sum += nums[index]
            index += 1
        present = set(nums)
        while prefix_sum in present:
            prefix_sum += 1
        return prefix_sum