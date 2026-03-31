class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            if (
                row == ROWS or col == COLS or
                min(row, col) < 0 or
                grid[row][col] == "0"
            ):
                return
            
            grid[row][col] = "0"
            for dr, dc in directions:
                dfs(row + dr, col + dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    num_islands += 1
        
        return num_islands