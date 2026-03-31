class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        candidates.sort()


        def backtrack(i: int, curr_sum: int = 0):
            if curr_sum == target:
                if subset not in result:
                    result.append(subset[:])
                return
            
            if i >= len(candidates) or curr_sum > target:
                return
            
            # pick i and add it to the sum
            # i + 1 for both rec calls to avoid duplicates
            subset.append(candidates[i])
            backtrack(i + 1, curr_sum + candidates[i])

            # skip i and do not add it to the sum
            subset.pop()
            backtrack(i + 1, curr_sum)

        backtrack(0)
        return result