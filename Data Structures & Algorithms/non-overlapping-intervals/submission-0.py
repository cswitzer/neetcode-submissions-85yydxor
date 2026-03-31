class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        res = 0
        intervals = sorted(intervals)
        curr_end = intervals[0][1]

        # iterate through the intervals. If the target interval starts before the current
        # ends, then we know they are overlapping. We must choose to keep the interval
        # that ends FIRST to minimize our chances of overlapping intervals in the future
        for i in range(1, len(intervals)):
            if intervals[i][0] < curr_end:
                # we must "remove" an interval
                res += 1
                # remove the one that ends LAST
                curr_end = min(curr_end, intervals[i][1])
            else:
                # no removals happen, so just set the current end to the target interval's end
                curr_end = intervals[i][1]
        return res