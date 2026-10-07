class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        result = []

        def helper(s,left,right,open_p,close_p):
            counter = 0

            # Analysis
            while(right < len(s)):
                if(s[right]==open_p):
                    counter += 1
                elif(s[right]==close_p):
                    counter -= 1

                if(counter < 0):
                    break

                right += 1

            # Case 1
            if(counter < 0):
                while(left <= right):
                    # Remove only the close_paranthesis if we encounter opening
                    # paranthesis we skip it.
                    if(s[left] != close_p):
                        left += 1
                        continue
                    
                    # Skip duplicate removals
                    if(left > 0 and s[left] == s[left - 1]):
                        left += 1
                        continue
                    
                    # Remove s[left]
                    new_str = s[:left] + s[left+1:]
                    helper(new_str,left,right,open_p,close_p)
                    left += 1
                
                return

            # Case 2
            elif(counter>0):
                reverse_str = s[::-1]
                helper(reverse_str,0,0,close_p,open_p)
                return
            
            # Case 3
            else:
                # Original Direction
                if(open_p == '('):
                    result.append(s)
                # Reversed Direction
                else:
                    result.append(s[::-1])

        helper(s,0,0,'(',')')

        return result