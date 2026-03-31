class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i: int, current: list[int]):
            if i >= len(nums):
                result.append(current[:])
                return
            
            # choose i
            current.append(nums[i])
            backtrack(i + 1, current)

            # not choose i
            current.pop()
            backtrack(i + 1, current)

        backtrack(0, [])
        return result