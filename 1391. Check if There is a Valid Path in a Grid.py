class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        w, n, e, s = 0, 1, 2, 3

        # (dy, dx, next entrance)
        to_east = (0, 1, w)
        to_west = (0, -1, e)
        to_north = (-1, 0, s)
        to_south = (1, 0, n)

        # (0 - from west, 1 - from north, 2 - from east, 3 - from south)
        path = [None,
            (to_east, None, to_west, None),   # 1═
            (None, to_south, None, to_north), # 2║
            (to_south, None, None, to_west),  # 3╗
            (None, None, to_south, to_east),  # 4╔
            (to_north, to_west, None, None),  # 5╝
            (None, to_east, to_north, None),  # 6╚
        ]

        M, N = len(grid), len(grid[0])

        for side in w, n, e, s:
            r, c = 0, 0

            while 0 <= r < M and 0 <= c < N:
                if path[grid[r][c]][side] is None: break
                if r == M - 1 and c == N - 1: return True

                dy, dx, side = path[grid[r][c]][side]
                r, c = r + dy, c + dx

                if r == 0 and c == 0: return False

        return False