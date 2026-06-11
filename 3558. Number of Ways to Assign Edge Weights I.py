class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:

        n = len(edges) + 1
        g = [[] for _ in range(n + 1)] # edges for each node
        for u, v in edges:
            if u < v:
                g[u].append(v) # bidirected ? no, only small -> large
            else:
                g[v].append(u) # bidirected

        d = [-1] * (n + 1) # depths
        d[1] = 0  # depth at 1 starting
        q = deque([1]) 
        while q:
            u = q.popleft()
            for v in g[u]:
                if d[v] < 0: # haven't checked depth
                    d[v] = d[u] + 1 # use partenth depth + 1
                    q.append(v) # queue to check childs later

        m = max(d[1:]) # get the max depth for node 1 
        MOD = 10**9 + 7 # constant
        return pow(2, m - 1, MOD) # power
