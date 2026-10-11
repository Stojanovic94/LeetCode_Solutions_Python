class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        for i in range(1,len(nums)+1):
            if n%i == 0:
                total_sum = total_sum + nums[i-1]**2
        return total_sum