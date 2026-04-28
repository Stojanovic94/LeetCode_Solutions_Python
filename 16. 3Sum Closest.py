class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]  

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, n-1

            min_sum = nums[i] + nums[i+1] + nums[i+2]
            if min_sum >= target:
                if abs(min_sum - target) < abs(res - target):
                    res = min_sum
                break
            
            max_sum = nums[i] + nums[-1] + nums[-2]
            if max_sum <= target: 
                if abs(max_sum - target) < abs(res - target):
                    res = max_sum
                continue

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s-target) < abs(res-target):
                    res = s

                if s < target:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif s > target:
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                else:
                    return target  

        return res