class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            min_heap.append([distance, [x, y]])
        
        heapq.heapify(min_heap)
        result = []
        for i in range(k):
            point = heapq.heappop(min_heap)[1]
            result.append(point)
        
        return result