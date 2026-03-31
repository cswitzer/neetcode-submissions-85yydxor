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

            subset.append(nums[i])
            backtrack(i, curr_sum + nums[i])

            subset.pop()
            backtrack(i + 1, curr_sum)

        backtrack(0)
        return result