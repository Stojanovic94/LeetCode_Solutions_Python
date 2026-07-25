class Solution:
    def maxProduct(self, n: int) -> int:
        d1, d2 = sorted(str(n))[-2:]
        return int(d1) * int(d2)