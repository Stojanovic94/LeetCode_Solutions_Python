class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans=0
        a=max(nums)
        for i  in nums:
            ans+=(a-i)
        return ans