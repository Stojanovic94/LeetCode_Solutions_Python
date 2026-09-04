class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        vmax = [nums[0]] * n
        vmin = [nums[-1]] * n
        for i in range(1, n):
            vmax[i] = max(vmax[i - 1], nums[i])
            vmin[n - 1 - i] = min(vmin[n - i], nums[n - 1 - i])
        for i in range(n):
            if vmax[i] - vmin[i] <= k:
                return i
        return -1