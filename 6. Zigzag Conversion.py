class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        offset = 0
        res = ""

        constJump = (numRows - 1) * 2

        if numRows == 1:
            return s

        for i in range(0, length, max(1, constJump)):
            res += s[i]

        for i in range(1, numRows - 1):
            offset += 2
            j = i

            while (j + constJump - offset) < length:
                res += s[j]
                res += s[j + constJump - offset]

                j += constJump
            
            if j < length:
                res += s[j]

        for i in range((numRows - 1), length, constJump):
            res += s[i]

        return res
            