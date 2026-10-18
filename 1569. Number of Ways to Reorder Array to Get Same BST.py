class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        prev = [i - 1 for i in range(n + 2)]
        next = [i + 1 for i in range(n + 2)]

        size = [0] * (n + 2)

        mul = 1

        for x in reversed(nums):
            size[x] = 1

            left = prev[x]
            if size[left] > 0:
                size[x] += size[left]
                
                pl = prev[left]
                prev[x] = pl
                next[pl] = x

            right = next[x]
            if size[right] > 0:
                size[x] += size[right]

                nr = next[right]
                prev[nr] = x
                next[x] = nr

            mul = mul * size[x] % MOD

        fac = 1 
        for i in range(2, n + 1):
            fac = fac * i % MOD

        return (fac * pow(mul, -1, MOD) - 1) % MOD