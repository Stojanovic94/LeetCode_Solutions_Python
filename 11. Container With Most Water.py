class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height) - 1
        maxh = max(height)
        result = 0
        while i < j:
            if result > maxh *(j-i):
                return result
            elif height[i] > height[j]:
                result = max(result,height[j]*(j - i))
                j -=1
            else:
                result = max(result,height[i]*(j - i))
                i += 1
        return result            