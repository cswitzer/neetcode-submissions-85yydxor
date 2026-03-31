class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:        
        result = []
        i = 0
        n = len(intervals)

        # Add all intervals whose last value is less than newInterval's first value
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals as long as the current interval in intervals starts
        # BEFORE the new interval. This check always works due to the loop above, which already
        # adds all intervals that come before the newInterval already
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
