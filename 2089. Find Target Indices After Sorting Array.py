class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        lenn = len(nums)
        l, r = 0, lenn - 1
        ans = []
        ans_set = set()
        if nums[l] == nums[r] and nums[l] == target:
            return list(range(0, lenn))
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                ans_set.add(mid)
                if mid + 1 < lenn and nums[mid + 1] == target:
                    ans_set.add(mid + 1)
                if mid + 2 < lenn and nums[mid + 2] == target:
                    ans_set.add(mid + 2)
                if mid - 1 > 0 and nums[mid - 1] == target:
                    ans_set.add(mid - 1)
                r = mid - 1
        ans = sorted(list(ans_set))
        return ans