class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        candidates.sort()


        def backtrack(i: int, curr_sum: int = 0):
            if curr_sum == target:
                result.append(subset[:])
                return
            
            if i >= len(candidates) or curr_sum > target:
                return
            
            # pick i and add it to the sum
            # i + 1 for both rec calls to avoid duplicates
            subset.append(candidates[i])
            backtrack(i + 1, curr_sum + candidates[i])

            # skip i altogether e.g. [1, 1, 2], skips all the ones and goes to two
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            subset.pop()
            backtrack(i + 1, curr_sum)

        backtrack(0)
        return result