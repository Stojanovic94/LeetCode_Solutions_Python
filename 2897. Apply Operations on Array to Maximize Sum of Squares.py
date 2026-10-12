class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        x = 1
        base = []
        while x <= 1000000000:
            base.append(x)
            x = x << 1
        nb = len(base)
        count = [0] * nb

        for x in nums:
            for i, y in enumerate(base):
                if x & y:
                    count[i] += 1
        
        x = [0] * k
        for i in range(nb):
            for j in range(min(k, count[i])):
                x[j] += base[i]
                
        res = 0
        for y in x:
            res = (res + y * y) % 1000000007
        return res