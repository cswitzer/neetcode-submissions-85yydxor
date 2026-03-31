class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m is row, n is col
        cache = [[0 for col in range(n)] for row in range(m)]

        def memo(row: int, col: int, rows: int, cols: int) -> int:
            if row == rows or col == cols:
                return 0
            if cache[row][col] > 0:
                return cache[row][col]
            if row == rows - 1 and col == cols - 1:
                return 1
            
            cache[row][col] = memo(row + 1, col, rows, cols) + memo(row, col + 1, rows, cols)
            return cache[row][col]

        return memo(0, 0, m, n)
            