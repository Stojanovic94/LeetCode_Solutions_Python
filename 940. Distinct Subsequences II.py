class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10 ** 9 + 7

        dp = 1  # empty subsequence
        last = {}

        for ch in s:
            new_dp = (dp * 2 - last.get(ch, 0)) % MOD
            last[ch] = dp
            dp = new_dp

        return (dp - 1) % MOD