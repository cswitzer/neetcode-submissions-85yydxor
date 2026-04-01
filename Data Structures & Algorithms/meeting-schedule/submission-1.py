"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        
        intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(1, len(intervals)):
            prev_interval = intervals[i - 1]
            curr_interval = intervals[i]
            if curr_interval.start < prev_interval.end:
                return False
        return True