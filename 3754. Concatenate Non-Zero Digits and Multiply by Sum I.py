class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        digits = []
        n2 = n
        while n2:
            d = n2%10
            if d>0:
               digits.append(d)
            n2 = n2 // 10
        s = sum(digits)
        ans = 0
        for i, d in enumerate(digits):
            ans += (d*10**i)
        return ans*s