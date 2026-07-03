from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        costs = set()

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            costs.add(w)

        # Topological sort (DAG)
        topo = []
        q = deque([i for i in range(n) if indegree[i] == 0])

        while q:
            u = q.popleft()
            topo.append(u)

            for v, w in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        costs = sorted(costs)

        def can(min_edge):
            INF = float('inf')
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                # intermediate offline nodes not allowed
                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < min_edge:
                        continue

                    if v != n - 1 and v != 0 and not online[v]:
                        continue

                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

            return dist[n - 1] <= k

        left, right = 0, len(costs) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            val = costs[mid]

            if can(val):
                ans = val
                left = mid + 1
            else:
                right = mid - 1

        return ans