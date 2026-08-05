class Solution: # O(n+i) TC, O(n+i) SC
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
        
        suspicious = [False]*n
        suspicious[k] = True

        q = deque([k])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    q.append(v)

        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))
        return [i for i in range(n) if not suspicious[i]]  




        