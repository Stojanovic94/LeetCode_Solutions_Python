class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        thieves = deque([])
        mDist = [ [-1]*n for i in range(n) ]
        for i in range(n):
            for j in range(n):
                if (grid[i][j] == 1):
                    thieves.append( (i,j) )
                    mDist[i][j] = 0
        if (mDist[0][0] == 0 or mDist[-1][-1] == 0):
            return 0

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while (thieves):
            r, c = thieves.popleft()
            for rOS, cOS in dirs:
                adjR, adjC = rOS+r, cOS+c
                if (0 <= adjR < n and 0 <= adjC < n and mDist[adjR][adjC] == -1):
                    mDist[adjR][adjC] = mDist[r][c] + 1
                    thieves.append((adjR, adjC))
        
        travel = deque([(mDist[0][0], 0, 0)])
        visited = [ [False]*n for i in range(n) ]
        visited[0][0] = True
        ans = min(mDist[0][0], mDist[-1][-1])
        
        while (travel):
            safety, r, c = travel.popleft()
            ans = min(safety, ans)
            if (r == n-1 and c == n-1):
                return ans

            for rOS, cOS in dirs:
                adjR, adjC = rOS+r, cOS+c
                if (0 <= adjR < n and 0 <= adjC < n and not visited[adjR][adjC]):
                    visited[adjR][adjC] = True
                    nextSafety = min(mDist[adjR][adjC], safety)
                    if (nextSafety < ans):
                        travel.append( (nextSafety, adjR, adjC) )
                    else:
                        travel.appendleft( (nextSafety, adjR, adjC) )
            # print(travel)

        return -1