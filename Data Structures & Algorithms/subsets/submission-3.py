class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []

        def dfs(nums: List[int], subset: List[int], subsets: List[int]):
            subsets.append(subset[:])
            for i in range(len(nums)):
                subset.append(nums[i])
                dfs(nums[i + 1:], subset, subsets)
                subset.pop()
        
        dfs(nums, subset, subsets)
        return subsets
