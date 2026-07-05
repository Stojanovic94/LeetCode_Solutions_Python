class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board[0])
        f = [[-inf, 0] for _ in range(n + 1)]
        f[1] = [0, 1]
        for j in range(1, n):
            c = board[0][j]
            if c == 'X': break
            f[j + 1] = [f[j][0] + int(c), 1]

        for i, s in enumerate(board[1:]):
            tmp = f[0][:]
            for j, c in enumerate(s):
                if c == 'X':
                    tmp = f[j + 1][:]
                    f[j + 1] = [-inf, 0]
                    continue
                if c in 'ES': c = '0'
                max_v = max(tmp[0], f[j][0], f[j + 1][0])
                n_path = 0
                if max_v == tmp[0]: n_path += tmp[1]
                if max_v == f[j][0]: n_path += f[j][1]
                if max_v == f[j + 1][0]: n_path += f[j + 1][1]
                tmp = f[j + 1][:]
                f[j + 1] = [max_v + int(c), n_path % 1000000007]
        res = f[-1]
        if res[0] < 0: res[0] = 0
        return res