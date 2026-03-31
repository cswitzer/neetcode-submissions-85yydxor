class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        memo = {}
        def dfs(i: int, target: int) -> bool:
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            if (i, target) in memo:
                return memo[(i, target)]

            # add num at i or skip it
            pick = dfs(i + 1, target - nums[i])
            skip = dfs(i + 1, target)
            memo[(i, target)] = pick or skip
            return memo[(i, target)]
        
        return dfs(0, sum(nums) // 2)

