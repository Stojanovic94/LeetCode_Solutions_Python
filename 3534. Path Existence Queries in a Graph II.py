from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Step 1: Identify distinct values and their indices
        distinct_vals = sorted(list(set(nums)))
        m = len(distinct_vals)
        val_to_idx = {v: i for i, v in enumerate(distinct_vals)}
        
        # Step 2: Identify components based on maxDiff
        # Two values are in the same component if they are connected through values in nums
        # with gaps at most maxDiff.
        comp_id = [0] * m
        curr_id = 0
        for i in range(1, m):
            if distinct_vals[i] - distinct_vals[i - 1] > maxDiff:
                curr_id += 1
            comp_id[i] = curr_id
        
        # Step 3: Build the binary lifting table for shortest paths
        # f[p][i] stores the furthest index reachable from i in 2^p jumps.
        max_p = m.bit_length()
        if max_p == 0: max_p = 1
        
        f = [None] * max_p
        f0 = [0] * m
        right = 0
        for i in range(m):
            while right + 1 < m and distinct_vals[right + 1] <= distinct_vals[i] + maxDiff:
                right += 1
            f0[i] = right
        f[0] = f0
        
        for p in range(1, max_p):
            f_prev = f[p - 1]
            f[p] = [f_prev[f_prev[i]] for i in range(m)]
        
        # Step 4: Process queries
        results = []
        for u, v in queries:
            if u == v:
                results.append(0)
                continue
            
            vu, vv = nums[u], nums[v]
            if vu == vv:
                results.append(1)
                continue
            
            if vu > vv:
                vu, vv = vv, vu
            
            iu, iv = val_to_idx[vu], val_to_idx[vv]
            
            # If the values are in different components, no path exists
            if comp_id[iu] != comp_id[iv]:
                results.append(-1)
                continue
            
            # Use binary lifting to find the minimum distance from iu to iv.
            # We find the largest number of jumps that still leave us at an index less than iv.
            steps = 0
            curr = iu
            for p in range(max_p - 1, -1, -1):
                fp = f[p]
                if fp[curr] < iv:
                    curr = fp[curr]
                    steps += (1 << p)
            
            # The distance is the number of steps to reach just before iv, plus one last jump.
            results.append(steps + 1)
            
        return results