class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        i = 0
        sign = 1
        
       
        while i < len(s) and s[i] == " ":
            i += 1
        
       
        if i == len(s):
            return 0
        
        
        if s[i] == "+":
            sign = 1
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
        
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            
            if num > 214748364 or (num == 214748364 and digit > (7 if sign == 1 else 8)):
                return 2147483647 if sign == 1 else -2147483648
            
            num = num * 10 + digit
            i += 1
        
        
        return sign * num