MIN_K = 2
K_RANGE = range(MIN_K, 6)
INVERSES = [[1], [1, 2], [1, 0, 3], [1, 3, 2, 4]]

class Solution:
    def resultArray4(self, nums: List[int]) -> List[int]:
        counts = [0] * 4
        running_counts = [0] * 4
        zero_end = 0
        past_last_odd_mult = 0
        product = 1
        for i, num in enumerate(nums):
            if num % 4 == 0:
                for j in range(4):
                    running_counts[j] = 0
                zero_end = i + 1
                past_last_odd_mult = 0
                product = 1
            elif num % 2 == 0:
                for j in range(4):
                    running_counts[j] = 0
                if past_last_odd_mult > 0:
                    zero_end = past_last_odd_mult
                past_last_odd_mult = i + 1
                product = 1
            else:
                product = (product * num) % 4
                for j in range(1, 4):
                    if INVERSES[4-MIN_K][j-1] == 0:
                        continue
                    counts[(product*INVERSES[4-MIN_K][j-1])%4] += running_counts[j]
                counts[product] += 1
                running_counts[product] += 1
            counts[0] += zero_end
            if past_last_odd_mult > zero_end:
                counts[2] += past_last_odd_mult - zero_end
        return counts
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return [n * (n + 1) // 2]
        if k == 4:
            return self.resultArray4(nums)
        counts = [0] * k
        running_counts = [0] * k
        invertible_start = 0
        product = 1
        for i, num in enumerate(nums):
            if num % k == 0:
                for j in range(k):
                    running_counts[j] = 0
                invertible_start = i + 1
                product = 1
            else:
                product = (product * num) % k
                for j in range(1, k):
                    counts[(product*INVERSES[k-MIN_K][j-1])%k] += running_counts[j]
                counts[product] += 1
                running_counts[product] += 1
            counts[0] += invertible_start
        return counts