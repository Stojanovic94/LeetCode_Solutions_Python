class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")" : "(",
            "]": "[",
            "}": "{"
        }
        
        stack = []

        for ch in s:
            if ch not in mapping:
                stack.append(ch)
            
            else:
                if not stack:
                    return False
                
                else:
                    popped = stack.pop()
                    if popped != mapping[ch]:
                        return False
        
        return not stack
            