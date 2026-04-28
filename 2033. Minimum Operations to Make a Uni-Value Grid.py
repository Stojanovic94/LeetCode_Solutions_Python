class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        mod = None
        for row in grid:
            for val in row:
                if mod is None:
                    mod = val % x
                elif val % x != mod:
                    return -1
        vals = []
        for row in grid:
            for val in row:
                vals.append(val)
        vals.sort()
        half = len(vals) // 2
        if half == 0:
            return 0
        return (sum(vals[-half:]) - sum(vals[:half])) // x