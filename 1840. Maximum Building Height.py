class Solution:
    def maxBuilding(self, n: int, re: List[List[int]]) -> int:
        re.sort(key=lambda i:i[0]+i[1])
        ans, b = 0, [1,0]
        for r in re:
            ans = max(ans,(min(2*n-b[0]+b[1],r[0]+r[1])-(b[0]-b[1]))//2)
            if b[0]-b[1] < r[0]-r[1]: b = [r[0],r[1]]
        return max(ans,n-b[0]+b[1])