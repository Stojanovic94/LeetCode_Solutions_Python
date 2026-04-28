class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        counts = Counter(nums)
        zero_count = counts.pop(0, 0)
        result = [[0, 0, 0]] if zero_count >= 3 else []
        if len(counts) <= 1:
            return result
        unique = list(counts)
        for num in unique:
            if num < 0 and zero_count:
                if -num in counts:
                    result.append([num, 0, -num])
            if not num % 2:
                candidate = -num // 2
                if counts[candidate] >= 2:
                    result.append([num, candidate, candidate])
        a = -unique[-1] // 2 
        b = unique[0]
        if a > b:
            start = bisect_right(unique, a)
        else:
            start = bisect_right(unique, b)
        a = -(unique[0] // 2)
        b = unique[-1]
        if a < b:
            stop = bisect_left(unique, a)
        else:
            stop = bisect_left(unique, b)
        for i in range(start, stop):
            num = unique[i]
            j = bisect_right(unique, -num * 2) if num < 0 else i + 1
            k = bisect_right(unique, -unique[0] - num)
            for right in unique[j:k]:
                left = -num - right
                if left in counts:
                    result.append([left, num, right])
        return result