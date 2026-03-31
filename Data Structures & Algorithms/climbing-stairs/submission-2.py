class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(i: int):
            if i == n:
                return 1
            if i > n:
                return 0

            if i in cache:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        
        return dfs(0)
