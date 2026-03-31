class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def num_hours(k: int) -> int:
            """k is the eating rate per hour"""
            return sum(math.ceil(pile / k) for pile in piles)
        
        l, r = 1, max(piles)
        k = r
        while l <= r:
            mid = l + (r - l) // 2
            hours = num_hours(mid)
            if hours <= h:
                r = mid - 1
                k = mid
            else:
                l = mid + 1
        return k