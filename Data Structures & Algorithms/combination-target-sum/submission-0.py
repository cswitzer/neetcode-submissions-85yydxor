class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol_set = []

        def dfs(i: int, target: int):
            if target < 0 or i >= len(nums):
                return

            if target == 0:
                res.append(sol_set.copy())
                return
            
            sol_set.append(nums[i])
            dfs(i, target - nums[i])

            sol_set.pop()
            dfs(i + 1, target)

        dfs(0, target)
        return res