class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        def feasible(k: int):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h

        while left <= right:
            k = left + (right - left) // 2
            if feasible(k):
                right = k - 1
            else:
                left = k + 1
        
        return left

        