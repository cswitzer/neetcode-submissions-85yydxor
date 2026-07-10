class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 1:
            return max_profit

        l = 0
        for r in range(1, len(prices)):
            curr_profit = prices[r] - prices[l]
            max_profit = max(max_profit, curr_profit)
            if prices[r] < prices[l]:
                l = r

        return max_profit