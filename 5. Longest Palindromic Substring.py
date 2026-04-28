class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n <= 1 or s == s[::-1]:
            return s

        x, ml = 0, 1

        for i in range(1, n):
            de = i - ml
            do = de - 1
            o = s[do : i + 1]
            ev = s[de : i + 1]

            if do >= 0 and o == o[::-1]:
                x = do
                ml += 2

            elif ev == ev[::-1]:
                x = de
                ml += 1

        return s[x:ml+x]