class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = [False]*n

        def bfs(node):
            visit[node] = True
            que = deque([node])
            node_ct = 0
            edge_ct = 0
            while que:
                curr = que.popleft()
                node_ct += 1
                edge_ct += len(adj[curr])

                for nei in adj[curr]:   
                    if visit[nei]:
                        continue
                    visit[nei] = True
                    que.append(nei)
            edge_ct //= 2
            return edge_ct == (node_ct)*(node_ct-1) // 2
        
        res = 0
        for i in range(n):
            if not visit[i]:
                res += bfs(i)

        return res