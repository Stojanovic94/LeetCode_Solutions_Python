class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # a-z:97,122
        # A-Z:65,90
        res = [0]*26
        seen_upper, seen_lower = set(), set()
        for c in word:
            if ord(c)>96 and c not in seen_lower:
                res[97-ord(c)]+= 1
                seen_lower.add(c)
            if ord(c)<91 and c not in seen_upper:
                res[65-ord(c)]+= 1
                seen_upper.add(c)
        ans = 0
        for num in res:
            if num==2:
                ans+=1
        return ans