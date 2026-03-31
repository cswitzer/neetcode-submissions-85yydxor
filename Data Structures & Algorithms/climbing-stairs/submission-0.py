class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        cache = [-1] * (n + 1)
        cache[1] = 1  # One way to climb one step
        cache[2] = 2  # Two ways to climb two steps (1+1 or 2)

        def dfs(i: int) -> int:
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = dfs(i - 1) + dfs(i - 2)
            return cache[i]

        return dfs(n)