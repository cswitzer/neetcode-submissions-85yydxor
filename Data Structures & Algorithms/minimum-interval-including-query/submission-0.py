class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals)
        min_heap = []
        res = {}
        i = 0
        for q in sorted(queries):
            # keep adding to the min_heap while q is in between each interval (inclusive)
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1
            
            # keep popping from the min_heap while the end is less than q
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # NOTE: The above two loops only work because we sort both intervals and queries above
            res[q] = min_heap[0][0] if min_heap else -1
        return [res[q] for q in queries]