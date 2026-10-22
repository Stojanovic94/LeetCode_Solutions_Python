from typing import List

class Solution:
    """
    The problem asks for the minimum number of operations to sort a permutation 
    of [0, 1, ..., n-1] using two operations:
    1. Reverse the entire array (R)
    2. Rotate Left by One (L)

    These two operations generate the Dihedral group D_n, which consists of 2n 
    possible states for any initial array:
    - n cyclic shifts: L^k(nums) for k in [0, n-1]
    - n cyclic shifts of the reversed array: L^k(reverse(nums)) for k in [0, n-1]

    This is equivalent to finding the shortest path in the Cayley graph of D_n 
    starting from the identity (initial array) to the sorted state.
    The nodes are states v_k = L^k(nums) and w_k = L^k(reverse(nums)).
    The costs (edge weights) are 1 for L and 1 for R.

    The shortest path distances from the initial state v_0 are:
    - Distance to v_k: min(k, n - k + 2)
      (k steps via L...L, or n-k+2 steps via R L^{n-k} R)
    - Distance to w_k: min(k + 1, n - k + 1)
      (k+1 steps via R L^k, or n-k+1 steps via L^{n-k} R)
    """

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        res = float('inf')
        target = list(range(n))
        
        # Candidate 1: The sorted state is a cyclic shift of the original array.
        # Since it's a permutation of 0..n-1, if any cyclic shift is sorted, 
        # it must be the one that starts with 0.
        k = nums.index(0)
        # Check if L^k(nums) == [0, 1, ..., n-1]
        # In Python, slicing and list comparison is O(n) and typically faster than loops.
        if nums[k:] + nums[:k] == target:
            # Min operations to reach L^k(nums) is min(k, (n-k) + 2)
            res = min(res, k, n - k + 2)
            
        # Candidate 2: The sorted state is a cyclic shift of the reversed array.
        # Similarly, the only candidate is the cyclic shift starting with 0.
        rev_nums = nums[::-1]
        k_rev = rev_nums.index(0)
        # Check if L^k_rev(rev_nums) == [0, 1, ..., n-1]
        if rev_nums[k_rev:] + rev_nums[:k_rev] == target:
            # Min operations to reach L^k_rev(reverse(nums)) is min(k_rev + 1, (n-k_rev) + 1)
            # Paths: R then L^k_rev (1+k_rev) OR L^{n-k_rev} then R (n-k_rev+1)
            res = min(res, k_rev + 1, n - k_rev + 1)
            
        # If no sorted state was reached, it is impossible.
        if res == float('inf'):
            return -1
        
        return int(res)