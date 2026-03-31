class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row: int, col: int) -> int:
            if (
                min(row, col) < 0 or
                row == ROWS or col == COLS or
                grid[row][col] == 0
            ):
                return 0
            
            grid[row][col] = 0
            down = dfs(row + 1, col)
            up = dfs(row - 1, col)
            left = dfs(row, col + 1)
            right = dfs(row, col - 1)
            return 1 + down + up + left + right

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(max_area, area)
        
        return max_area