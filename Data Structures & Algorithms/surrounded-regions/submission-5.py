class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        ROWS, COLS = len(board), len(board[0])

        # think of the problem backwards. For example:
        # 1. Instead of capture all surrounded regions
        # 2. Think, capture all regions except the unsurrounded ones

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or
                c == COLS or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
            
        # 1. Capture unsurrounded regions (O -> T)
        # We only run this on the borders because any O that is on the border is unsurrounded,
        # and any O connected to that one is also unsurrounded
        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):

                # 2. Capture surrounded regions (O -> X)
                if board[r][c] == "O":
                    board[r][c] = "X"

                # 3. Uncapture unsurrounded regions (T -> O)
                elif board[r][c] == "T":
                    board[r][c] = "O"