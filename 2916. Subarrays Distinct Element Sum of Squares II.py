from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        SHIFT = 40
        MASK = (1 << SHIFT) - 1
        bit = [0] * (n + 1)
        last = {}
        totC = 0
        totS = 0
        g = 0
        ans = 0
        for j in range(n):
            v = nums[j]
            p = last.get(v, -1)
            if p < 0:
                R = totS + totC
            else:
                i = p + 1
                q = 0
                while i > 0:
                    q += bit[i]
                    i -= i & (-i)
                cSuf = totC - (q >> SHIFT)
                sSuf = totS - (q & MASK)
                R = sSuf - p * cSuf
                d = -((1 << SHIFT) + p)
                i = p + 1
                while i <= n:
                    bit[i] += d
                    i += i & (-i)
                totC -= 1
                totS -= p
            d = (1 << SHIFT) + j
            i = j + 1
            while i <= n:
                bit[i] += d
                i += i & (-i)
            totC += 1
            totS += j
            g += 2 * R + (j - p)
            ans += g
            last[v] = j
        return ans % MOD