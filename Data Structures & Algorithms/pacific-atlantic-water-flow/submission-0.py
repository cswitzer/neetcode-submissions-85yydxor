class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r: int, c: int, visit: Set, prev_height: int):
            if ((r, c) in visit or
                r < 0 or c < 0 or r == ROWS or c == COLS or
                heights[r][c] < prev_height):
                return
            
            # can reach ocean, check all neighbors based on the above conditions
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])


        # go from the ocean to the cells, so we are looking for cells that 
        # are greater instead of smaller
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        return [list(cell) for cell in pac & atl]