class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []
        nums.sort()

        def dfs(i: int):
            subsets.append(subset[:])
            
            if i >= len(nums):
                return

            # start from curr index i to prevent duplicates
            for j in range(i, len(nums)):
                # if in the same recursive level and the previous element is one we already processed,
                # then skip it
                if j > i and nums[j] == nums[j - 1]:
                    continue
                subset.append(nums[j])
                dfs(j + 1)
                subset.pop()

        dfs(0)
        return subsets