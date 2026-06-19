class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        1. Row 0 has 1, 2, and 3
        2. Represent this with a dictionary where row is an int and nums in that row is a set
        3. length of board is 9x9, so subsquares are all 3x3
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                num = board[r][c]
                if num == ".":
                    continue
                if num in rows[r] or num in cols[c] or num in squares[(r // 3, c // 3)]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                squares[(r // 3, c // 3)].add(num)
        return True
