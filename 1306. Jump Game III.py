class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        
        q = deque([start])
        visited = [False] * n
        visited[start] = True
        while q:
            node = q.popleft()
            if arr[node] == 0:
                return True
            left, right = node - arr[node], node + arr[node]
            if left >= 0 and not visited[left]:
                q.append(left)
                visited[left] = True
            if right < n and not visited[right]:
                q.append(right)
                visited[right] = True
        return False
        