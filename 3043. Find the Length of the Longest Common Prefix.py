class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for a in arr1:
            while a > 0:
                if a in prefixes:
                    break
                prefixes.add(a)
                a = a // 10

        r = 0
        for b in arr2:
            while b > r:
                if b in prefixes:
                    r = b
                    break
                b = b // 10
                
        return len(str(r)) if r else 0 

    

        