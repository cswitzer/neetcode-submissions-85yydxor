"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda x: x.start)
        # The top of the heap represents the earliest time a meeting ends
        min_heap = []

        for interval in intervals:
            # If the meeting that ends the earliest ends before the start, we will reuse that room
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
        
        return len(min_heap)
