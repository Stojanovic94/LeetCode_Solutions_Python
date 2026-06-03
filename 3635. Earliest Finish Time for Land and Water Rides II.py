from math import inf
def earliestFinishTime(firstStartTime: List[int], firstDuration: List[int], secondStartTime: List[int], secondDuration: List[int]) -> int:
    earliest_first_end = inf
    for i, start in enumerate(firstStartTime):
        end = start + firstDuration[i]
        if earliest_first_end > end:
            earliest_first_end = end
    #print(earliest_first_end)
    earliest_end = inf
    for i, start in enumerate(secondStartTime):
        end = (start if start >= earliest_first_end else earliest_first_end) + secondDuration[i]
        if earliest_end > end:
            earliest_end = end
    #print(earliest_end)
    return earliest_end

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        return min(earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration),
                    earliestFinishTime(waterStartTime, waterDuration, landStartTime, landDuration))