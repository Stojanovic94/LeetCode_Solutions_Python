import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        return self.Dijkstra(n, self.edges2table(n, edges), labels, k)

    def edges2table(self, n, edges):
        table = [[] for _ in range(n)]
        for u, v, w in edges:
            table[u].append((v, w))

        return table

    def Dijkstra(self, n: int, table: list[list[tuple]], labels: str, k: int):
        visited = [False for _ in range(n)]

        q = [(0, 0, 1, labels[0])]

        while q:
            weight, now, cnt, last_char = heapq.heappop(q)

            if now == n - 1:
                return weight

            if visited[now]:
                continue

            for v, w in table[now]:
                if visited[v]:
                    continue

                if last_char == labels[v]:
                    if cnt + 1 > k:
                        continue
                    heapq.heappush(q, (weight + w, v, cnt + 1, last_char))
                    visited[now] = True
                else:
                    heapq.heappush(q, (weight + w, v, 1, labels[v]))
                    visited[now] = True

        return -1