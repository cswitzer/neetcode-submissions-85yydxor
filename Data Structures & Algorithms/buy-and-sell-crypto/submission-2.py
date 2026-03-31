class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_idx = 0
        for sell_idx in range(1, len(prices)):
            # we found a new lowest prices
            if prices[sell_idx] < prices[buy_idx]:
                buy_idx = sell_idx
            else:
                curr_profit = prices[sell_idx] - prices[buy_idx]
                max_profit = max(max_profit, curr_profit)
        return max_profit