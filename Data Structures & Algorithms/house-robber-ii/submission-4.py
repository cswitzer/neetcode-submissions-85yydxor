class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        without_first = nums[1:]
        without_last = nums[:-1]

        def dfs(i: int, numbers: List[int], cache: Dict[int, int]):
            if i >= len(numbers):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(
                numbers[i] + dfs(i + 2, numbers, cache),
                dfs(i + 1, numbers, cache),
            )
            return cache[i]
        
        return max(
            dfs(0, numbers=nums[1:], cache={}), 
            dfs(0, numbers=nums[:-1], cache={}),
        )