class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        solution = []

        def dfs(i: int, sum_so_far: int = 0):
            if sum_so_far == target:
                result.append(solution[:])
                return

            if sum_so_far > target or i >= len(nums):
                return
            
            solution.append(nums[i])
            dfs(i, sum_so_far + nums[i])
            solution.pop()
            dfs(i + 1, sum_so_far)
        
        dfs(0)
        return result