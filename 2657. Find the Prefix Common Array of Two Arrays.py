class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        res = []
        cnt = 0
        for i in range(len(A)):
            if A[i] in seen:
                cnt += 1
            else:
                seen.add(A[i])
            if B[i] in seen:
                cnt += 1
            else:
                seen.add(B[i])
            res.append(cnt)
        return res