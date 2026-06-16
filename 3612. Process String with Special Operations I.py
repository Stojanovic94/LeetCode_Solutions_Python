class Solution:
    def processStr(self, s: str) -> str:
        ans = ""

        for x in s:
            if x == '*':
                ans = ans[:-1]

            elif x == '#':
                ans += ans

            elif x == '%':
                ans = ans[::-1]

            else:
                ans +=x

        return ans