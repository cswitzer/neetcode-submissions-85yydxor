class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def steps(i: int):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(steps(i + 1), steps(i + 2))
            return memo[i]

        return min(steps(0), steps(1))