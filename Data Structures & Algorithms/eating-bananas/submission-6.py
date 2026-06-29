class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def num_hours(k: int):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            return hours
        
        min_rate = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            k = l + (r - l) // 2
            if num_hours(k) <= h:
                min_rate = k
                r = k - 1
            else:
                l = k + 1
        return min_rate