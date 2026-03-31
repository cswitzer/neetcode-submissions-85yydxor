class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= len(nums) - 1:
                return 0  # reached the end

            res = float('inf')
            furthest = min(len(nums) - 1, i + nums[i])

            for next_i in range(i + 1, furthest + 1):
                res = min(res, 1 + dfs(next_i))

            dp[i] = res
            return res
        
        return dfs(0)