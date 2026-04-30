class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        nums.sort()
        n = len(nums)
        
        for i in range(n - 3):
                       
            # Skip duplicated number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Check min
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break            
            # Check max
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue

            for j in range(i + 1, n - 2):

                # Skip duplicated number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Check min
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break            
                # Check max
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                
                sum_1_2 = nums[i] + nums[j]

                left = j + 1
                right = n - 1

                while left < right:
                    total = sum_1_2 + nums[left] + nums[right]

                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        answer.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1    

                        left += 1
                        right -= 1
        
        return answer
                
                
                