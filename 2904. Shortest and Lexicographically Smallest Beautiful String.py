class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        cnt1 = 0 
        left = 0 
        ans = s 
        if s.count('1') < k:
            return ''

        for right, x in enumerate(s):
            if x == '1':
                cnt1 += int(x)

            while cnt1 > k or s[left] == '0':

                cnt1 -= int(s[left])
                left += 1 
            if cnt1 == k:
                 t = s[left: right + 1]
                 if len(t) < len(ans) or len(t) == len(ans) and t < ans:
                    ans = t
        return ans 