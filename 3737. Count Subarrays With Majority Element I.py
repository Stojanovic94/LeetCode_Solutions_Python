class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        t = target
        cnt = [0] * (n*2+2)
        acc = [0] * (n*2+2)
        pre = n+1
        cnt[pre]=1
        acc[pre]=1
        res =0
        for num in nums:
            if t==num:
                pre+=1
            else:
                pre-=1
            cnt[pre]+=1
            acc[pre] = acc[pre-1] + cnt[pre]
            res+=acc[pre-1]
        return res