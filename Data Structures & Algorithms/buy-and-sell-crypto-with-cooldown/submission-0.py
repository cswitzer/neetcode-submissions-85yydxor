class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        State: Buying or selling?
        If Buy -> i + 1
        If Sell -> i + 2 for cooldown

        Our decisions are based on if we are buying or selling on day i
        Key = (i, buying) val=max_profit
        """

        dp = {}

        def dfs(i: int, buying: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                # we can sell or cooldown
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # we can sell or cooldown
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        
        return dfs(0, True)
    