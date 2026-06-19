class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        curr = 0

        for change in gain:
            curr += change
            res = max(curr, res)

        return res
        