class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        sol = []

        def backtrack(i: int):
            if len(sol) == k:
                result.append(sol[:])
                return
            
            # bound i between 1 and n
            if i > n:
                return
            
            sol.append(i)
            backtrack(i + 1)

            sol.pop()
            backtrack(i + 1)
        
        backtrack(1)
        return result