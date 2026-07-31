class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = [word.count(chr(ord('a') + i)) for i in range(26)] 
        arr = sorted(counts, reverse=True)
        total = 0
        for group, i in enumerate(range(0, len(arr), 8), start=1):
            total += sum(arr[i:i+8]) * group

        return total