class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while stones and len(stones) > 1:
            first = -1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)
            if first == second:
                continue
            else:
                new_stone = -1 * (first - second)
                heapq.heappush(stones, new_stone)
        return -1 * stones[0] if stones else 0