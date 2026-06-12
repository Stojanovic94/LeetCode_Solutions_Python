MX = 100001
mod = 10**9+7
fac = [1]*MX
for i in range(1,MX):
    fac[i] = fac[i-1]*(i)%mod
inv = [1]*MX
inv[-1] = pow(fac[-1],mod-2,mod)
for i in range(MX-2,-1,-1):
    inv[i] = inv[i+1]*(i+1)%mod
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges)+1
        deep = [0]*(n+1)
        g = [[] for _ in range(n+1)]
        q = [[] for _ in range(n+1)]
        ans = [0]*(len(queries))
        vis = [False] * (n+1)
        father = [i for i in range(n+1)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        for idx,[u,v] in enumerate(queries):
            q[u].append((v,idx))
            q[v].append((u,idx))
        
        def find(x):
            while father[x]!=x:
                father[x] = father[father[x]]
                x = father[x]
            return father[x]
        
        def tarjan(u,parent):
            vis[u] = True
            for v in g[u]:
                if v == parent:
                    continue
                tarjan(v,u)
                father[v] = u
            
            for node,idx in q[u]:
                if vis[node]:
                    ans[idx] = find(node)
        tarjan(1,0)
        def f(u,fa,d):
            nonlocal deep
            deep[u] = d
            for v in g[u]:
                if v==fa:continue
                f(v,u,d+1)
        f(1,0,0)
        res = [0]*len(queries)
        def comb(n,a):
            return fac[n]*inv[a]*inv[n-a]%mod
        def f1(x):
            ret = 0
            for i in range(1,x+1,2):
                ret = (ret + comb(x,i))%mod
            return ret
        for i,[a,b] in enumerate(queries):
            lca = ans[i]
            x = deep[a]+deep[b] - 2*deep[lca]
            if x == 0:
                res[i] = 0
            else:
                res[i] = pow(2, x-1, mod)
        return res
        
        