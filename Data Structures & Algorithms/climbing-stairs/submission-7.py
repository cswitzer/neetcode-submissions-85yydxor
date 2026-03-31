class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def steps(i: int):
            if i <= 1:
                return 1
            if i in cache:
                return cache[i]
                
            cache[i] = steps(i - 1) + steps(i - 2)
            return cache[i]
        
        return steps(n)
        