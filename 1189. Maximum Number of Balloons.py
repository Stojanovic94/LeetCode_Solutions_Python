from itertools import accumulate

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        # dp[v] stores the number of valid sequences of current length ending with value v.
        # We use 1-based indexing for values (1 to m), so dp has size m + 1.
        # dp[0] is a dummy 0.
        # Initially for length 1, any value from 1 to m is valid.
        dp = [0] + [1] * m
        
        for i in range(2, n + 1):
            # Compute prefix sums of the current dp array.
            # pref[k] = sum(dp[0]...dp[k])
            pref = list(accumulate(dp))
            
            if i % 2 == 0:
                # For even length i, the relation is a_{i-1} < a_i.
                # dp[v] = sum(dp[u] for u < v) = pref[v-1]
                dp = [0] + pref[:-1]
            else:
                # For odd length i, the relation is a_{i-1} > a_i.
                # dp[v] = sum(dp[u] for u > v) = pref[m] - pref[v]
                total = pref[-1]
                dp = [0] + [(total - x) % MOD for x in pref[1:]]
        
        # Sum valid sequences for one pattern (starting with <) and multiply by 2 for symmetry.
        return (sum(dp) % MOD * 2) % MOD