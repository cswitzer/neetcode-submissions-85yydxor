class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        solutions = []
        candidates.sort()

        def backtrack(i: int, current: int):
            if current == 0:
                result.append(solutions[:])
                return
            elif current < 0 or i >= len(candidates):
                return
            
            solutions.append(candidates[i])
            backtrack(i + 1, current - candidates[i])

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            solutions.pop()
            backtrack(i + 1, current)
        
        backtrack(0, target)
        return result