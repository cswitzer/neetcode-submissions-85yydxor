class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Combinations restrict order
        Permutations restrict reuse
        """
        result = []
        perm = []
        used = set()

        def dfs():
            if len(perm) == len(nums):
                result.append(perm[:])
                return

            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                perm.append(nums[i])
                dfs()
                used.remove(i)
                perm.pop()
        
        dfs()
        return result
          