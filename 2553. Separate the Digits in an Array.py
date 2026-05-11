class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            if num > 9:
                for d in str(num):
                    res.append(int(d))
            else:
                res.append(num)

        return res