class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        # prefixes = [0]
        # for num in nums:
        #     prefixes.append(num + prefixes[-1])
        
        # target = prefixes[-1] - x
        target = sum(nums) - x
        if target == 0:
            return n
        elif target < 0:
            return -1

        res = -1
        currsum = 0
        l = 0
        for r in range(n):
            currsum += nums[r]
            while currsum > target:
                currsum -= nums[l]
                l += 1
            
            if currsum == target:
                res = max(res, (r - l + 1))    
        return n - res if res != -1 else -1