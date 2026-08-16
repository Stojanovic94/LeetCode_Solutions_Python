from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]
        for x in stones:
            cnt[x % 3] += 1
        
        c0, c1, c2 = cnt
        
        if c1 == 0 and c2 == 0:
            return False
        
        if c0 % 2 == 0:
            return c1 > 0 and c2 > 0
        else:
            return abs(c1 - c2) > 2