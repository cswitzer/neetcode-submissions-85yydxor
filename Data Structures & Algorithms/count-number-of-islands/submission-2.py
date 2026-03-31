class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            if r == ROWS or r < 0 or c == COLS or c < 0 or grid[r][c] == "0":
                return 0
            
            # set this and surronding islands as visited
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return 1
        
        num_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                num_islands += dfs(r, c)
        
        return num_islands