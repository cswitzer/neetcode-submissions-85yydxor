class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        The order in which we pop the ballons matters, as the neihbors will change
        It appears the state will be dp[i]

        """
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l: int, r: int) -> int:
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            # how many balloons if we pop i LAST!
            # this means subarrays at left and right of i are FIXED, making DP possible.
            # we cannot look at this problem as what will happen if we pop i first
            # because neighbors will change in that case, making DP impossible
            # this also make i the out of bound left and right bounds when solving subproblems
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)
