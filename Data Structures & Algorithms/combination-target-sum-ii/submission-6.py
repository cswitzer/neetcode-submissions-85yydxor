class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        curr_comb = []
        candidates.sort()

        def dfs(start: int, curr_sum: int, target: int):
            if curr_sum == target:
                results.append(curr_comb[:])
                return
            
            if start >= len(candidates) or curr_sum > target:
                return
            
            for i in range(start, len(candidates)):
                # skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                curr_comb.append(candidates[i])
                dfs(i + 1, curr_sum + candidates[i], target)
                curr_comb.pop()

        dfs(0, 0, target)
        return results