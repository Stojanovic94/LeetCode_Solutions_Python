class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sorted_intervals = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)], key=lambda x: x[1])
        ends = [x[1] for x in sorted_intervals]
        dp = [[(0, ())] * 5 for _ in range(n + 1)]

        for i in range(1, n + 1):
            l, r, w, idx = sorted_intervals[i - 1]
            prev_idx = bisect.bisect_left(ends, l) - 1 + 1
            for k in range(1, 5):
                best_w, best_indicies = dp[i - 1][k]
                prev_w, prev_indicies = dp[prev_idx][k - 1]
                cand_w = prev_w + w
                cand_indicies = tuple(sorted(prev_indicies + (idx, )))

                if cand_w > best_w:
                    best_w, best_indicies = cand_w, cand_indicies
                elif cand_w == best_w and cand_w > 0:
                    if not best_indicies or cand_indicies < best_indicies:
                        best_indicies = cand_indicies

                dp[i][k] = (best_w, best_indicies)
        max_score = 0
        ans = ()
        for k in range(1, 5):
            score, idx_list = dp[n][k]
            if score > max_score:
                max_score = score
                ans = idx_list
            elif score == max_score and score > 0:
                if not ans or idx_list < ans:
                    ans = idx_list
        return list(ans)