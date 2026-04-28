class Solution:
    def containsCycle(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        last_row = rows - 1
        last_col = cols - 1

        # parent[x] < 0 means x is a root, and -parent[x] is the component size
        parent = [-1] * (rows * cols)

        gr = grid
        par = parent
        c = cols

        for r in range(last_row):
            row = gr[r]
            down_row = gr[r + 1]
            base = r * c

            # cols 0..last_col-1: can check both right and down
            for col in range(last_col):
                idx = base + col
                ch = row[col]

                # right neighbor
                if ch == row[col + 1]:
                    a = idx
                    while par[a] >= 0:
                        pa = par[a]
                        gpa = par[pa]
                        if gpa >= 0:
                            par[a] = gpa
                        a = pa

                    b = idx + 1
                    while par[b] >= 0:
                        pb = par[b]
                        gpb = par[pb]
                        if gpb >= 0:
                            par[b] = gpb
                        b = pb

                    if a == b:
                        return True

                    if par[a] > par[b]:
                        a, b = b, a

                    par[a] += par[b]
                    par[b] = a

                # down neighbor
                if ch == down_row[col]:
                    a = idx
                    while par[a] >= 0:
                        pa = par[a]
                        gpa = par[pa]
                        if gpa >= 0:
                            par[a] = gpa
                        a = pa

                    b = idx + c
                    while par[b] >= 0:
                        pb = par[b]
                        gpb = par[pb]
                        if gpb >= 0:
                            par[b] = gpb
                        b = pb

                    if a == b:
                        return True

                    if par[a] > par[b]:
                        a, b = b, a

                    par[a] += par[b]
                    par[b] = a

            # last column: only down neighbor remains
            ch = row[last_col]
            if ch == down_row[last_col]:
                idx = base + last_col

                a = idx
                while par[a] >= 0:
                    pa = par[a]
                    gpa = par[pa]
                    if gpa >= 0:
                        par[a] = gpa
                    a = pa

                b = idx + c
                while par[b] >= 0:
                    pb = par[b]
                    gpb = par[pb]
                    if gpb >= 0:
                        par[b] = gpb
                    b = pb

                if a == b:
                    return True

                if par[a] > par[b]:
                    a, b = b, a

                par[a] += par[b]
                par[b] = a

        # last row: only right neighbors remain
        row = gr[last_row]
        base = last_row * c

        for col in range(last_col):
            if row[col] == row[col + 1]:
                idx = base + col

                a = idx
                while par[a] >= 0:
                    pa = par[a]
                    gpa = par[pa]
                    if gpa >= 0:
                        par[a] = gpa
                    a = pa

                b = idx + 1
                while par[b] >= 0:
                    pb = par[b]
                    gpb = par[pb]
                    if gpb >= 0:
                        par[b] = gpb
                    b = pb

                if a == b:
                    return True

                if par[a] > par[b]:
                    a, b = b, a

                par[a] += par[b]
                par[b] = a

        return False