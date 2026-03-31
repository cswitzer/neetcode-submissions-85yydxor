class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        sol = []

        def backtrack(i: int):
            if i >= len(nums):
                result.append(sol[:])
                return
            
            sol.append(nums[i])
            backtrack(i + 1)

            sol.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return result