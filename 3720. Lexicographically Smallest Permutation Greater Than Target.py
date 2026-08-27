INVALID='{'
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        c=Counter(s)
        n=len(s)
        endi = n
        for i in range(n):
            ch = target[i]
            if ch not in c:
                endi = i
                break
            else:
                c[ch]-=1
                if c[ch]==0: c.pop(ch)
        if endi==n:
            endi=n-1
            c[target[endi]]+=1
        # print(c, endi)
        for i in range(endi, -1, -1):
            ch = target[i]
            x=INVALID
            for y in c.keys():
                if y>ch and y<x: x=y
            if x!=INVALID:
                res=[target[:i], x]
                c[x]-=1
                for y in sorted(c.keys()):
                    res.append(y*c[y])
                return ''.join(res)
            elif i>0:
                c[target[i-1]]+=1
        return "" 
        # print(endi, c)
        # return s

        