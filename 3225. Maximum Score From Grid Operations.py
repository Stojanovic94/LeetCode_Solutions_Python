class Solution:
    def maximumScore(self, grid: list[list[int]]) -> int:
        n = len(grid)
        pref = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                pref[j][i + 1] = pref[j][i] + grid[i][j]

        dp = [[-float('inf')] * (n + 1) for _ in range(2)]
        for h in range(n + 1):
            dp[0][h] = 0

        for j in range(1, n):
            new_dp = [[-float('inf')] * (n + 1) for _ in range(2)]
            
            p_max = -float('inf')
            for h in range(n + 1):
                p_max = max(p_max, dp[0][h] - pref[j-1][h])
                new_dp[0][h] = max(new_dp[0][h], p_max + pref[j-1][h])
            
            p_max = -float('inf')
            for h in range(n, -1, -1):
                p_max = max(p_max, dp[0][h], dp[1][h])
                new_dp[1][h] = max(new_dp[1][h], p_max + pref[j][h] - pref[j][h]) 

            p_max = -float('inf')
            for h in range(n, -1, -1):
                p_max = max(p_max, dp[0][h], dp[1][h])
                if h < n + 1:
                    new_dp[0][0] = max(new_dp[0][0], p_max)

            p_max = -float('inf')
            for h in range(n, -1, -1):
                p_max = max(p_max, dp[0][h] + pref[j][h], dp[1][h] + pref[j][h])
                new_dp[1][h] = max(new_dp[1][h], p_max - pref[j][h])
            
            p_max = -float('inf')
            for h in range(n + 1):
                p_max = max(p_max, dp[1][h])
                new_dp[1][h] = max(new_dp[1][h], p_max)

            p_max = -float('inf')
            for h in range(n + 1):
                p_max = max(p_max, dp[0][h], dp[1][h])
                new_dp[0][h] = max(new_dp[0][h], p_max)
                
            dp = new_dp

        res = 0
        for state in range(2):
            for h in range(n + 1):
                res = max(res, dp[state][h])
        return res