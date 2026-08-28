class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n, cnt = len(s), Counter(s)
        odds = [c for c, v in cnt.items() if v % 2]
        if len(odds) > n % 2:
            return ""

        mid, h = (odds[0] if odds else ""), n // 2
        pool = Counter({c: v // 2 for c, v in cnt.items()})
        build = lambda half: half + mid + half[::-1]

        stop = 0                                     # longest prefix of target[:h] the pool can match
        while stop < h and pool[target[stop]]:
            pool[target[stop]] -= 1
            stop += 1

        if stop == h and (p := build(target[:h])) > target:
            return p                                 # half forced -> exactly one candidate

        for i in range(stop, -1, -1):                # walk back to the last raisable position
            if i < h and (c := min((x for x in pool if x > target[i] and pool[x]), default="")):
                pool[c] -= 1
                return build(target[:i] + c + "".join(c * pool[c] for c in sorted(pool)))
            if i:
                pool[target[i - 1]] += 1             # un-consume, restoring the pool for i-1

        return ""