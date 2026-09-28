class Solution:
    def maxDepth(self, s: str) -> int:

        local_max=0
        overall_max=0

        for char in s:
            if char == '(':
                local_max+=1
            elif char == ')':
                local_max-=1
            

            overall_max=max(local_max,overall_max)
        
        return overall_max
        