class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!= len(goal):
            return False
        
        res=s+s
        if goal in res:
            return True 
        return False