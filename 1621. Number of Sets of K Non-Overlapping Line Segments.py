class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # g0 + s0 + g1 + s1 + g2  => k+1 g's and k s's 
        # all gaps sum to n-1 i.e g0 + s0 + g1 + s1 + g2 = n-1 where s >= 1 and g >= 0
        # g0 + s0' + g1 + s1' + g2 = n-1 where s' >= 0
        # g0 + s0 + g1 + s1 + g2 = n-1-k here k =2
        # now total elements on left = k + k+1 = 2k+1
        # applying formula n+k-1 C k-1 here we get => n-1-k + 2k+1 - 1 C 2k+1 -1 = n + k - 1 C 2k 
        return math.comb(n+k-1,2*k)%(10**9+7)