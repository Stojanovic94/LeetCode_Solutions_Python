class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])
        stack = []
        ans = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                total_val = grid[r][c]
                grid[r][c] = 0
                stack.append((r, c))

                while stack:
                    row, col = stack.pop()

                    new_row = row + 1
                    if new_row != m and grid[new_row][col] != 0:
                        stack.append((new_row, col))
                        total_val += grid[new_row][col]
                        grid[new_row][col] = 0

                    new_row = row - 1
                    if new_row != -1 and grid[new_row][col] != 0:
                        stack.append((new_row, col))
                        total_val += grid[new_row][col]
                        grid[new_row][col] = 0

                    new_col = col + 1
                    if new_col != n and grid[row][new_col] != 0:
                        stack.append((row, new_col))
                        total_val += grid[row][new_col]
                        grid[row][new_col] = 0

                    new_col = col - 1
                    if new_col != -1 and grid[row][new_col] != 0:
                        stack.append((row, new_col))
                        total_val += grid[row][new_col]
                        grid[row][new_col] = 0

                if total_val % k == 0:
                    ans += 1

        return ans