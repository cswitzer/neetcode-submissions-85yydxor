class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        solution = []

        def backtrack(i: int, current: int):
            if current == 0:
                result.append(solution[:])
                return
            elif current < 0 or i >= len(nums):
                return

            # Choose the current num and add it to the sum
            solution.append(nums[i])
            backtrack(i, current - nums[i])

            # Skip the current number and exclude it from the sum
            solution.pop()
            backtrack(i + 1, current)

        backtrack(0, target)
        return result            
