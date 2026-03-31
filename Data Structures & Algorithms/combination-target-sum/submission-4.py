class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i: int, curr_sum: int = 0):
            if curr_sum == target:
                result.append(subset[:])
                return
            
            if curr_sum > target or i >= len(nums):
                return

            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j, curr_sum + nums[j])
                subset.pop()

        backtrack(0)
        return result