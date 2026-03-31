class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Check if one of the top, bottom, left, or right elements is an "x"
        if I am on "o". If "x", return true. If "o", keep checking. If 
        out of bounds, return false
        """
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        o_pos = set()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    o_pos.add((r, c))
        
        def dfs(r: int, c: int):
            # O is not bounded by X
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return False

            if board[r][c] == "X":
                return True
            
            if (r, c) in visited:
                return True
            
            visited.add((r, c))

            return all([
                dfs(r + 1, c),
                dfs(r - 1, c),
                dfs(r, c + 1),
                dfs(r, c - 1),
            ])

        # If we modify the board in-place, we risk flipping O's that were NOT
        # originally surrounded by X's
        to_flip = set()
        for pos in o_pos:
            r, c = pos
            visited = set()
            if dfs(r, c):
                to_flip.add((r, c))

        for (r, c) in to_flip:
            board[r][c] = "X"