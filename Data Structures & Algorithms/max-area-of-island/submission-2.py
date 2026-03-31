class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r: int, c: int):
            if r == ROWS or r < 0 or c == COLS or c < 0 or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))
            curr_area = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return curr_area
        
        for r in range(ROWS):
            for c in range(COLS):
                curr_area = dfs(r, c)
                self.max_area = max(self.max_area, curr_area)
        
        return self.max_area