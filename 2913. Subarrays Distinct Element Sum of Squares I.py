class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 1
        prev = 1
        dp = [1]
        last = {}
        last[nums[0]] = 0
        for i in range(1, len(nums)):
            new_dp = [0] * (i + 1)
            ls = last[nums[i]] if nums[i] in last else -1
            cur = prev + 2 * (sum(dp[ls + 1:])) + i - ls
            ans += cur
            for j in range(ls + 1):
                new_dp[j] = dp[j]
            for j in range(ls + 1, i):
                new_dp[j] = dp[j] + 1
            new_dp[-1] = 1

            prev = cur
            dp = new_dp
            last[nums[i]] = i
        return ans