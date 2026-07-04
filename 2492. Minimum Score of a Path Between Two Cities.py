class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n+1))
        self.min_weights = [float("inf")] * (n+1)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y, weight):
        x, y = self.find(x), self.find(y)
        new_weight = min(self.min_weights[x], self.min_weights[y], weight)
        if x != y:
            self.parents[x] = y
            self.min_weights[y] = new_weight
            return True
        else:
            self.min_weights[x] = new_weight
            return False
            

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        uf = UnionFind(n)
        for u, v, w in roads:
            uf.union(u, v, w)
        return uf.min_weights[uf.find(1)]
            