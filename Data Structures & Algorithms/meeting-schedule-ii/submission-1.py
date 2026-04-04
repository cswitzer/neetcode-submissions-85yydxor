"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([intervals[i].start for i in range(len(intervals))])
        end   = sorted([intervals[i].end for i in range(len(intervals))])
        min_rooms = count = 0
        s = e = 0

        while s < len(intervals) and e < len(intervals):
            # A new meeting starts before the earliest ends...
            if start[s] < end[e]:
                count += 1
                s += 1
            # A meeting has ended...
            else:
                count -= 1
                e += 1
            min_rooms = max(min_rooms, count)

        return min_rooms
