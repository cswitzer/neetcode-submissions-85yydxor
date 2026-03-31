class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        origin is (0, 0)
        From points, find the k closest origins
        """
        distances = []
        for point in points:
            x, y = point
            distance = math.sqrt((x - 0) ** 2 + (y - 0) ** 2)
            heapq.heappush(distances, (distance, point))
        
        k_closest = []
        for _ in range(k):
            point = heapq.heappop(distances)[1]
            k_closest.append(point)
        return k_closest