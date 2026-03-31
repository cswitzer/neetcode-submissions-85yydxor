class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        def dfs(i: int):
            if i in dp:
                return dp[i]
            if i >= len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            
            # the index at i is only the MAX jump distance. We can jump any distance
            # from (i + 1) to nums[i]
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                if dfs(j):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        return dfs(0)