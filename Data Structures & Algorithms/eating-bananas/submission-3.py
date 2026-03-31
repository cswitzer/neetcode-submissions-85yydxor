class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles = [1, 4, 3, 2], h = 9
        output: 2

        explanation: with an eating rate of 2, we can eat all bananas in 6 hours

        1. Always at least 1 pile
        2. Hours is always greater than or equal to the length of the piles
        3. Each pile has AT LEAST 1 banana

        Greatest eating rate of piles: 4
        Least eating rate of piles: 1
        Eating rates will be between 1 and 4, or [1, 2, 3, 4]

        Get eating rate:
        hours = ceil(pile / eating rate) for all piles
        example:
            eating rate: 2
            piles = [1, 2, 3, 4]
            hours = ceil(1 / 2) + ceil(2 / 2) + ceil(3 / 2) + ceil(4 / 2) [answer 6]

        The return value is the minimum eating rate
        
        Binary search:
            formula: time (in hours) = total / eating rate
            bounds: low (e.g. 1) to high (e.g. 4)
            conditions:
                - if I find an eating rate that takes less than h, high = mid - 1
                since I want to find the minimum
                - if the eating rate takes more than h, then low = mid + 1 since my
                eating rate is too low
        
        [4, 10, 23, 25]
        4..25

        """
        def hours_needed(k: int) -> int:
            # with eating rate 'k', sum up how many hours it would take to
            # eat each pile
            return sum(math.ceil(p / k) for p in piles)

        low, high = 1, max(piles)
        answer = high
        while low <= high:
            mid = low + (high - low) // 2

            # We finished the bananas in time. Time to search to the left for new possible min
            if hours_needed(mid) <= h:
                answer = mid
                high = mid - 1
            # Didn't finish in time. Time to up our eating rate
            else:
                low = mid + 1
        
        return answer
