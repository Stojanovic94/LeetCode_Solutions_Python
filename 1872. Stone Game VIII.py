class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        for index in range(1, len(stones)):
            stones[index] += stones[index - 1]

        best = stones[-1]
        for index in range(len(stones) - 2, 0, -1):
            best = max(best, stones[index] - best)
        return best