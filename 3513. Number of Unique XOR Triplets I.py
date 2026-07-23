class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 2: 
            return 2
        
        if n == 1:
            return 1
        
        gb = 0
        while n >= (1 << gb):
            gb += 1

        return max((1 << gb) - 1, n) + 1
