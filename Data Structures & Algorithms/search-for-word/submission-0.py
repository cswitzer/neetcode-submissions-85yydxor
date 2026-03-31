class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        seen = set()

        def backtrack(r: int, c: int, i: int):
            if i == len(word):
                return True
            
            if (
                r == ROWS or r < 0 or
                c == COLS or c < 0 or
                (r, c) in seen or
                board[r][c] != word[i]
            ):
                return False

            seen.add((r, c))
            res = (backtrack(r + 1, c, i + 1) or
                   backtrack(r - 1, c, i + 1) or
                   backtrack(r, c + 1, i + 1) or
                   backtrack(r, c - 1, i + 1))
            seen.remove((r, c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False