@cache
def rec(i):
    if i == 0: return False

    for j in range(isqrt(i), 0, -1):
        if not rec(i-j**2): return True #any one of the recursive lower cases should be loss
    return False
ar = [rec(i) for i in range(100001)]

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return ar[n]