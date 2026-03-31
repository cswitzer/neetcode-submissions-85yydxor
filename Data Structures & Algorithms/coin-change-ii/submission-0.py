class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        coins = [1, 2, 3]
        amount = 4

        Must take coins until
        - amount is too high
        - amount is equal to the actual amount

        Unlimited amount of each coin in coins, so we can reuse a coin
        Combinations must be distinct

        What are my states:
        The state here would be (i, amount_left)

        base cases:
        if amount_left is 0:
            return sum of 1
        if amount_left is less than 0:
            return 0 since we went over
        if (i, amount_left) in dp:
            do not do repeated work

        recursive case:
        take coin at i
        do not take coin at i
        dp[(i, amount_left)] = dfs(i, amount_left - coins[i]) + dfs(i + 1, amount_left)
        return dp[(i, amount_left)]
        """
        dp = {}

        def dfs(i: int, amount_left: int):
            if amount_left == 0:
                return 1
            if amount_left < 0 or i >= len(coins):
                return 0
            if (i, amount_left) in dp:
                return dp[(i, amount_left)]
            
            dp[(i, amount_left)] = dfs(i, amount_left - coins[i]) + dfs(i + 1, amount_left)
            return dp[(i, amount_left)]

        return dfs(0, amount)
