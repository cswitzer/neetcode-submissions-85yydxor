class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        
        def dfs(i: int, prev: int) -> int:
            """
            [9, 1, 4, 2, 3, 3, 7]

            9 -> only itself
            1 -> 1, 4, 7 | 1, 2, 3, 7 | 1, 3, 7
            ...

            We can either include the current element or exclude it based on
            whether it is larger than the previous element

            Subproblems are also present. For example, when arriving at 3, the following character
            is 7. Therefore, we should not recompute the length of 3 repeatedly, since we already know
            it is 2

            base: i == len(nums) -> 0
            rcase: nums[i] > prev -> 1 unless prev is -1 (initial)
            """
            if i == len(nums):
                return 0

            if (i, prev) in dp:
                return dp[(i, prev)]
            
            take = 0
            skip = 0

            # include i since it is greater than i - 1
            if nums[i] > prev:
                take = 1 + dfs(i + 1, nums[i])
            
            # sometimes skipping may lead to a better result like in [1, 4, 2, 3]
            # where skipping 4 will lead to a better result 1, 2, 3
            skip = 0 + dfs(i + 1, prev)

            dp[(i, prev)] = max(take, skip)
            return dp[(i, prev)]
                
        return dfs(0, float("-inf"))
