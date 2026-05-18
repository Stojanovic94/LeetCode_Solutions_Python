class Solution:
    '''
    Approach 1:
        * DFS - return min(dfs(i+1), dfs(i-1), for j in sameVal[i]: dfs(j))
    Approach 2:
        * MultiSource BFS from start
    Approach 3:
        * Bidirectional multisource bfs - from start and end explore the path with lesser nodes in the layer
    '''
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        valueToIdx = {}
        for i, num in enumerate(arr):
            if num in valueToIdx:
                valueToIdx[num].append(i)
            else:
                valueToIdx[num] = [i]

        visited = {0, n-1}
        jumps = 0
        start = set([0])
        end = set([n-1])
        while start:
            if len(start) > len(end):
                start, end = end, start
            nextQ = set()
            for i in start:
                             
                for j in valueToIdx[arr[i]]:
                    if j in end:
                        return jumps+1
                    
                    if j not in visited:
                        nextQ.add(j)
                        visited.add(j)
                # clear list to prevent redundant search
                valueToIdx[arr[i]].clear()

                if i-1 in end or i+1 in end:
                    return jumps+1
                
                if i-1 >= 0 and i-1 not in visited:
                    nextQ.add(i-1)
                    visited.add(i-1)
    
                if i+1 < n and i+1 not in visited:
                    nextQ.add(i+1)
                    visited.add(i+1)
            jumps+=1
            start = nextQ
        return -1



        
            