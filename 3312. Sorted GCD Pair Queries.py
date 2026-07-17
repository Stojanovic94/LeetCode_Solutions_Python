import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        maxx = 0

        for i in range(len(nums)) :
            maxx = max(maxx, nums[i])
            prefixGcd.append(math.gcd(maxx, nums[i]))

        prefixGcd.sort()
        left = ans = 0
        right = len(prefixGcd) - 1

        while left < right :
            g = math.gcd(prefixGcd[left], prefixGcd[right])
            ans += g

            left += 1
            right -= 1

        return ans