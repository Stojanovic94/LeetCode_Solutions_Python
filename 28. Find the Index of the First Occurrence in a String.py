class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        # If the needle is longer than the haystack, it's impossible to find
        if m > n:
            return -1
        
        # Slide a window of size 'm' across the haystack
        for i in range(n - m + 1):
            # Check if the substring starting at i matches the needle
            if haystack[i : i + m] == needle:
                return i
        
        # If no match is found after the loop
        return -1
        