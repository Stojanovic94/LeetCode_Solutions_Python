class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Count total 1s in the original string
        ones = s.count('1')
        
        # Pad with '1' to correctly capture boundary 0-runs
        padded_s = '1' + s + '1'
        
        # Extract only valid, non-empty 0-runs
        zero_runs = [len(run) for run in padded_s.split('1') if run]
        
        # If there are fewer than two valid 0-runs, no trade pattern is possible
        if len(zero_runs) < 2:
            return ones
            
        # Find the maximum sum of any two adjacent valid 0-runs
        best = max(zero_runs[i] + zero_runs[i+1] for i in range(len(zero_runs) - 1))
        
        return ones + best