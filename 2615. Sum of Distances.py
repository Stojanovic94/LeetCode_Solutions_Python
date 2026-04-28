class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)

        indexes = defaultdict(list)
        for i in range(n):
            indexes[nums[i]].append(i)

        ans = [0] * n
        for num_indexes in indexes.values():
            if (count := len(num_indexes)) <= 1:
                continue
            
            prev_index, total_sum = 0, sum(num_indexes)
            for index in num_indexes:
                total_sum -= count * (index-prev_index)
                count -= 2
                ans[index] = total_sum
                prev_index = index

        return ans