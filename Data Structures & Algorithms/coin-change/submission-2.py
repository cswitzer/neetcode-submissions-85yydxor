class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.min_coins = float("infinity")
        dp = {}

        def dfs(i: int = 0, coin_count: int = 0, curr: int = 0):
            if curr == amount:
                self.min_coins = min(self.min_coins, coin_count)
            if curr > amount or i >= len(coins) or coin_count >= self.min_coins:
                return
            
            state = (i, curr)
            if state in dp and dp[state] <= coin_count:
                return
            
            dp[state] = coin_count
            dfs(i, coin_count + 1, curr + coins[i])        
            dfs(i + 1, coin_count, curr)
            
        dfs()
        return self.min_coins if self.min_coins < float("infinity") else -1
