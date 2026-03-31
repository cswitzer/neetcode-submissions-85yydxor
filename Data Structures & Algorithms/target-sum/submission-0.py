class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        We have two choices at each index i
        1. Add the number
        2. Subtract the number

        It looks like the state we want to keep track of is (i, value)

        base case:
        if value is target:
            return 1
        if i >= len(nums):
            return 0 because we didn't find a combination that adds to the target
        if (i, value) in dp:
            return dp at (i, value)

        Recursive case:
        add = dfs(i + 1, value + nums[i])
        sub = dfs(i + 1, value - nums[i])
        return add + sub
        """
        dp = {}

        def dfs(i: int, value: int):
            if i == len(nums) and value == target:
                return 1
            if i == len(nums):
                return 0
            if (i, value) in dp:
                return dp[(i, value)]
            
            add = dfs(i + 1, value + nums[i])
            sub = dfs(i + 1, value - nums[i])
            dp[(i, value)] = add + sub
            return dp[(i, value)]
        
        return dfs(0, 0)
