import numpy as np

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        
        A = np.array(nums, dtype=np.int64)
        
        # 1. Initial State: F(0) = \sum i * A[i]
        # This is a Dot Product (Projection of A onto the index basis)
        current_f = np.dot(np.arange(n), A)
        total_sum = np.sum(A)
        
        # 2. Vectorized Difference Propagation
        # The terms we subtract are n * A[n-1], n * A[n-2], ...
        # We can pre-calculate all 'deltas' in one pass
        # Delta_k = Total_Sum - n * A[n-1-k]
        deltas = total_sum - n * A[::-1]
        
        # 3. State Evolution
        # F(k) = F(0) + \sum_{i=0}^{k-1} deltas[i]
        # This is exactly what np.cumsum is designed for!
        f_values = np.zeros(n, dtype=np.int64)
        f_values[0] = current_f
        
        # We only need the first n-1 deltas to get all F(k)
        f_values[1:] = current_f + np.cumsum(deltas[:-1])
        
        return int(np.max(f_values))