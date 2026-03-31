class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row: int, col: int):
            if (
                row == ROWS or col == COLS or
                min(row, col) < 0 or
                grid[row][col] == "0"
            ):
                return
            
            # must set "1" to "0" so we do not recount the island
            grid[row][col] = "0"
            for dr, dc in directions:
                dfs(row + dr, col + dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands
