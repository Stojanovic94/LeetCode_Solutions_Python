class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        
        deltas = [0] * ((limit << 1) + 2)

        lp = 0
        rp = n - 1
        while lp < rp:
            left, right = nums[lp], nums[rp]
            if left <= right:
                small, large = left, right
            else:
                small, large = right, left
            
            deltas[small + 1] -= 1
            deltas[small + large] -= 1
            deltas[small + large + 1] += 1
            deltas[large + limit + 1] += 1

            lp += 1
            rp -= 1
        return n + min(accumulate(deltas))