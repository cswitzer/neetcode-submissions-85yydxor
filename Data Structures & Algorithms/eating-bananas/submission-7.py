class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def num_hours(k: int):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            return hours
        
        l, r = 1, max(piles)
        while l < r:
            k = l + (r - l) // 2
            if num_hours(k) <= h:
                r = k
            else:
                l = k + 1
        return l