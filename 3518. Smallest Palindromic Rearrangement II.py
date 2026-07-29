class Solution:
    def smallestPalindrome(self, S: str, K: int) -> str:
        import collections, math
        n = len(S)
        ans = [""] * n
        count = collections.Counter(S[: n // 2])
        if n & 1:
            ans[n // 2] = S[n // 2]
        tot = 0
        ways = 1
        i = 0
        for c in sorted(count, reverse=True):
            tot += count[c]
            ways *= math.comb(tot, count[c])
            if ways > K:
                for c2 in sorted(count):
                    if c2 >= c:
                        break
                    for loops in range(count[c2]):
                        ans[i] = ans[~i] = c2
                        i += 1
                    count[c2] = 0
        ways = 1
        tot = sum(count.values())
        for k in sorted(count):
            ways *= math.comb(tot, count[k])
            tot -= count[k]
        if ways < K:
            return ""
        tot = sum(count.values())
        while tot:
            for c in sorted(count):
                if count[c]:
                    ways2 = ways * count[c] // tot
                    if ways2 < K:
                        K -= ways2
                    else:
                        ans[i] = ans[~i] = c
                        i += 1
                        ways = ways2
                        count[c] -= 1
                        tot -= 1
                        break
        return "".join(ans)