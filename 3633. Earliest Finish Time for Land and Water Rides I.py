class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)

        minWaterEnd = min(waterStartTime[i] + waterDuration[i] for i in range(m))
        minLandEnd = min(landStartTime[i] + landDuration[i] for i in range(n))

        min_land_time = float("inf")
        for j in range(m):
            min_land_time = min(min_land_time, max(waterStartTime[j], minLandEnd) + waterDuration[j])
                
        min_water_time = float("inf")
        for j in range(n):
            min_water_time = min(min_water_time, max(landStartTime[j], minWaterEnd) + landDuration[j])

        return min(min_land_time, min_water_time)