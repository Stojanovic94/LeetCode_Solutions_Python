class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        low, high = 0, n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[high]:
                if nums[mid] >= target and nums[low] <= target:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] <= target and nums[high] >= target:
                    low = mid+1
                else:
                    high = mid-1
        return -1