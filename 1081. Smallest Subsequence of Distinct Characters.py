class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = {ch: 0 for ch in s}
        vis = set()
        stack = []

        for ch in s:
            freq[ch] += 1

        for ch in s:
            freq[ch] -= 1
            if ch in vis:
                continue
            while stack and stack[-1] > ch and freq[stack[-1]] > 0:
                vis.remove(stack.pop())
            stack.append(ch)
            vis.add(ch)

        return "".join(stack)