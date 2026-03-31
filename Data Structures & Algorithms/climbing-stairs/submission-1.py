class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(i: int) -> int:
            if i in cache:
                return cache[i]
            
            if i <= 1:
                cache[i] = 1
                return cache[i]

            return dfs(i - 1) + dfs(i - 2)
        
        return dfs(n)
