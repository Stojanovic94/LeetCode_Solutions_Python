class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        res = 0

        def fill_island(row, column):
            if row < 0 or column < 0 or row >= rows or column >= columns or grid[row][column] == 1:
                return

            grid[row][column] = 1

            fill_island(row + 1, column)
            fill_island(row - 1, column)
            fill_island(row, column + 1)
            fill_island(row, column - 1)
        
        for row in range(rows):
            for column in range(columns):
                if row == 0 or row == rows - 1 or column == 0 or column == columns - 1:
                    if grid[row][column] == 0:
                        fill_island(row, column)
        
        for row in range(1, rows - 1):
            for column in range(1, columns - 1):
                if grid[row][column] == 0:
                    res += 1
                    fill_island(row, column)
        return res