class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_set = set()
        max_length = -math.inf
        l = 0

        for r in range(len(s)):
            if s[r] not in character_set:
                max_length = max(r - l + 1, max_length)
            else:
                while s[r] in character_set:
                    character_set.remove(s[l])
                    l += 1
            
            character_set.add(s[r])
        return max_length if max_length != -math.inf else 0
                



            
  