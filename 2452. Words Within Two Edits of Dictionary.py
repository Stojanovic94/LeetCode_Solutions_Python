class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for query in queries:
            q = len(query)
            for word in dictionary:
                i = 0
                changes = 0
                while i < q:
                    if query[i] != word[i]:
                        changes += 1
                    if changes > 2:
                        break
                    i += 1
                if changes <= 2:
                    res.append(query)
                    break
        return res
