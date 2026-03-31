class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.graph = [["."] * n for i in range(n)]
        self.cols = set()
        self.pos_diags = set()
        self.neg_diags = set()

        def backtrack(r: int):
            if r >= n:
                # more than one solution, and we append them all here
                copy = ["".join(r) for r in self.graph]
                self.res.append(copy)
                return

            for c in range(n):
                if c in self.cols or (r + c) in self.pos_diags or (r - c) in self.neg_diags:
                    continue

                # add queen to current position
                self.cols.add(c)
                self.pos_diags.add(r + c)
                self.neg_diags.add(r - c)
                self.graph[r][c] = "Q"

                # try to place queen somewhere in the next row
                backtrack(r + 1)

                # remove queen at current position and try the next position
                self.cols.remove(c)
                self.pos_diags.remove(r + c)
                self.neg_diags.remove(r - c)
                self.graph[r][c] = "."     

        backtrack(0)
        return self.res