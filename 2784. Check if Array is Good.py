class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()

        max_ele = nums[-1]
        if len(nums) != max_ele + 1 or nums[-1] != nums[-1-1]:
            return False
        
        for i in range(max_ele - 1):
            if nums[i] != i + 1:
                return False
        return True