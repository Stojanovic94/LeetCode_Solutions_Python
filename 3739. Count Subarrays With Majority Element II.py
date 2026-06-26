class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        freq = [0] * (2 * n + 1)
        freq[n] = 1
        i = n
        res = 0
        pref = 0

        for num in nums:
            if num == target:
                pref += freq[i]
                i += 1
            else:
                i -= 1
                pref -= freq[i]

            freq[i] += 1
            res += pref
        
        return res