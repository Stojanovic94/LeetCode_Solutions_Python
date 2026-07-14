MOD = 1_000_000_007
MX = 201

lcms = [[lcm(i, j) for j in range(MX)] for i in range(MX)]

pow2 = [1] * MX
pow3 = [1] * MX
for i in range(1, MX):
    pow2[i] = pow2[i - 1] * 2 % MOD
    pow3[i] = pow3[i - 1] * 3 % MOD

mu = [0] * MX
mu[1] = 1
for i in range(1, MX):
    for j in range(i * 2, MX, i):
        mu[j] -= mu[i]

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        m = max(nums)

        cnt = [0] * (m + 1)
        for x in nums:
            cnt[x] += 1
        for i in range(1, m + 1):
            for j in range(i * 2, m + 1, i):
                cnt[i] += cnt[j]
                
        f = [[0] * (m + 1) for _ in range(m + 1)]
        for g1 in range(1, m + 1):
            for g2 in range(1, m + 1):
                l = lcms[g1][g2]
                c = cnt[l] if l <= m else 0
                c1, c2 = cnt[g1], cnt[g2]
                f[g1][g2] = (pow3[c] * pow2[c1 + c2 - c * 2] - pow2[c1] - pow2[c2] + 1) % MOD


        return sum(mu[j] * mu[k] * f[j * i][k * i]
                   for i in range(1, m + 1)
                   for j in range(1, m // i + 1)
                   for k in range(1, m // i + 1)) % MOD