# For each node, store a bitvector "path" where `path[i]` is set to 1
# iff there is a path to the node whose xor is `i`. To calculate the
# mask array for a node, first we OR the paths of the left and top cell.
# Then, if bit 0 of the node is set, we swap each pair of bits;
# if bit 1 is set, we swap each group of 2 bits; if bit 2 is set,
# we swap each group of 4 bits, etc.

# swapmask[0] will mask bits 0, 2, 4, 6, 8, 10, 12, 14, ...
# swapmask[1] will mask bits 0, 1, 4, 5, 8, 9, 12, 13, ...
# swapmask[2] will mask bits 0, 1, 2, 3, 8, 9, 10, 11, ...
sm = (1 << (512))-1
swapmasks = [0]*9 + [sm]
for i in range(8, -1, -1):
    sm ^= sm << (1 << i)
    swapmasks[i] = sm

def swap_for(path, cell):
    for i in range(10):
        if cell & (1 << i):
            path = ((path & swapmasks[i]) << (1 << i)) | ((path & (swapmasks[i] << (1 << i))) >> (1 << i))
    return path

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        paths = [0]*n
        xor = grid[0][0]
        paths[0] = 1 << xor
        for c in range(1, n):
            xor ^= grid[0][c]
            paths[c] = 1 << xor
        xor = grid[0][0]
        for r in range(1, m):
            xor ^= grid[r][0]
            paths[0] = 1 << xor
            for c in range(1, n):
                paths[c] = swap_for(paths[c-1] | paths[c], grid[r][c])

        return (paths[n-1] & -paths[n-1]).bit_length() - 1