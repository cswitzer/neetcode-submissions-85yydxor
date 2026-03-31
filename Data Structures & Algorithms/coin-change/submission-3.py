class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        
        def dfs(i: int, rem: int):
            if rem == 0:
                return 0
            
            if rem < 0 or i >= len(coins):
                return float("inf")

            if (i, rem) in dp:
                return dp[(i, rem)]

            pick = 1 + dfs(i, rem - coins[i])
            skip = dfs(i + 1, rem)
            
            dp[(i, rem)] = min(pick, skip)
            return dp[(i, rem)]

        ans = dfs(0, amount)
        return ans if ans != float("infinity") else -1
