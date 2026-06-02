class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        landEndTime = [landStartTime[i] + landDuration[i] for i in range(n)]
        waterEndTime = [waterStartTime[i] + waterDuration[i] for i in range(m)]

        min_land_end_time = min(landEndTime)
        min_water_end_time = min(waterEndTime)

        earliest_time = float("inf")

        for i in range(m):
            if waterStartTime[i] <= min_land_end_time:
                earliest_time = min(earliest_time, min_land_end_time + waterDuration[i])
            else:
                earliest_time = min(earliest_time, waterEndTime[i])
        
        for i in range(n):
            if landStartTime[i] <= min_water_end_time:
                earliest_time = min(earliest_time, min_water_end_time + landDuration[i])
            else:
                earliest_time = min(earliest_time, landEndTime[i])

        return earliest_time