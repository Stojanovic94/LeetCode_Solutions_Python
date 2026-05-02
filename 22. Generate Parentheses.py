class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def gen(curr, countO, countC):
            if countO == n and n == countC:
                output.append(curr)

            else:
                if countO < n:
                    gen(curr + "(", countO + 1, countC)

                if countC < countO:
                    gen(curr + ")", countO, countC + 1)

        gen("", 0, 0)
        return output
        