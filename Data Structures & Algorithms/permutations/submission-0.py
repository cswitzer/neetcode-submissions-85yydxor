class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        used = set()
        
        def dfs(perm: List[int]):
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            
            # for every position, try every element I have not used yet
            for i in range(0, len(nums)):
                if i in used:
                    continue
                used.add(i)
                perm.append(nums[i])
                dfs(perm)
                used.remove(i)
                perm.pop()
        
        dfs(perm)
        return result
          