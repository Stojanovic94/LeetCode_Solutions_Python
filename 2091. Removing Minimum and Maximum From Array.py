class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minn = min(nums)
        maks = max(nums)
        if minn == maks: return 1
        minn_i = nums.index(minn)
        maks_i = nums.index(maks)
        u = len(nums)

        print(minn_i, maks_i)

        if minn_i > maks_i:
            minn_i, maks_i = maks_i, minn_i


        cevap = min(minn_i + 1 + u-maks_i, max(minn_i, maks_i) + 1, u - min(minn_i, maks_i))

        return cevap

        