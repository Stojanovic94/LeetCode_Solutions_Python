class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        best = 0

        window = defaultdict(int)
        for right in range(len(s)):
            window[s[right]] += 1

            while window[s[right]] > 2:
                window[s[left]] -= 1
                left += 1
            
            best = max(best, right - left + 1)

        return best