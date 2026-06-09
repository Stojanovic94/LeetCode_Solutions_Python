class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxx = max(nums)
        minn = min(nums)
        return (maxx - minn) * k