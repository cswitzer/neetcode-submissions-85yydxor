class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1 * stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            biggest = -1 * heapq.heappop(max_heap)
            second_biggest = -1 * heapq.heappop(max_heap)
            if biggest == second_biggest:
                continue
            else:
                new_stone = -1 * (biggest - second_biggest)
                heapq.heappush(max_heap, new_stone)
        
        if not max_heap:
            return 0
            
        return -1 * max_heap[0]
            