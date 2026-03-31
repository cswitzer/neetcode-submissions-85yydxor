class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dp(house_index: int) -> int:
            if house_index >= len(nums):
                return 0

            if house_index in cache:
                return cache[house_index]
            
            rob_current = nums[house_index] + dp(house_index + 2)
            skip_current = dp(house_index + 1)

            cache[house_index] = max(rob_current, skip_current)
            return cache[house_index]

        return dp(0)