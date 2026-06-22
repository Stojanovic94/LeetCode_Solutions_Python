class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = defaultdict(int)
        word = "balloon"
        for t in text:
            if t in word:
                d[t] +=1
        
        if any(t not in d for t in word):
            return 0
        else:
            return min(d['b']//1, d['a']//1, d['l']//2, d['o']//2, d['n']//1)