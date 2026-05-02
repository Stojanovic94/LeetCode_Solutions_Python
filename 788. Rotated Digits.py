d={0:0,1:1,8:8,2:5,5:2,6:9,9:6}
ans=[0]*(10**4+1)
for val in range(1,10**4+1):
    ans[val]+=ans[val-1]
    s=str(val)
    cur=0
    for dig in s:
        cur*=10
        if dig in "347":
            break
        cur+=d[int(dig)]
    else:
        if cur!=val:
            ans[val]+=1
class Solution:
    def rotatedDigits(self, n: int) -> int:
        return ans[n]