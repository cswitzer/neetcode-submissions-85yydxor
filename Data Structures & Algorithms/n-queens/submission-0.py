class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.cols = set()
        self.neg_diags = set()
        self.pos_diags = set()
        self.grid = [["." for j in range(n)] for i in range(n)]
        result = []

        def dfs(r: int):
            if r == n:
                copy = ["".join(row) for row in self.grid]
                result.append(copy)
                return
            
            for c in range(n):
                if c in self.cols or r - c in self.neg_diags or r + c in self.pos_diags:
                    continue
                
                self.cols.add(c)
                self.neg_diags.add(r - c)
                self.pos_diags.add(r + c)
                self.grid[r][c] = "Q"

                # Go up a row after placing Q in the current column
                dfs(r + 1)

                # Back at r. Either there was 1 solution or no solution
                self.cols.remove(c)
                self.neg_diags.remove(r - c)
                self.pos_diags.remove(r + c)
                self.grid[r][c] = "."

        dfs(0)
        return result
                    