class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals = sorted(intervals)
        result = [intervals[0]]
        i = 0
        n = len(intervals)
        for i in range(1, n):
            # If the current interval result[-1] is overlapping with intervals[i],
            # we extend that interval. If they are not overlapping, we know intervals[i]
            # is the start of a new interval and append it
            if intervals[i][0] <= result[-1][1]:
                result[-1] = [
                    min(result[-1][0], intervals[i][0]),
                    max(result[-1][1], intervals[i][1]),
                ]
            else:
                result.append(intervals[i])
        return result