class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        
        if (num_thousands := num // 1000) > 0:
            ans.append("M" * num_thousands)
            num = num % 1000
        
        if (num_hundreds := num // 100) > 0:
            if num_hundreds == 9:
                ans.append("CM")
            elif num_hundreds >= 5:
                ans.append("D")
                ans.append("C" * (num_hundreds - 5))
            elif num_hundreds == 4:
                ans.append("CD")
            else:
                ans.append("C" * num_hundreds)
            num = num % 100
        
        if (num_tens := num // 10) > 0:
            if num_tens == 9:
                ans.append("XC")
            elif num_tens >= 5:
                ans.append("L")
                ans.append("X" * (num_tens - 5))
            elif num_tens == 4:
                ans.append("XL")
            else:
                ans.append("X" * num_tens)
            num = num % 10
        
        if num > 0:
            if num == 9:
                ans.append("IX")
            elif num >= 5:
                ans.append("V")
                ans.append("I" * (num - 5))
            elif num == 4:
                ans.append("IV")
            else:
                ans.append("I" * num)
        
        return "".join(ans)
            