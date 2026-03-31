class Solution:
    def _coord_valid(self, r: int, c: int, visited: Set, grid: List[List[int]]):
        """We should only add new coords to the queue if they are fresh fruits"""
        ROWS, COLS = len(grid), len(grid[0])
        if (
            0 <= r < ROWS and
            0 <= c < COLS and
            (r, c) not in visited and
            grid[r][c] == 1
        ):
            return True
        return False

    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minute = 0
        fresh = 0
        
        rotting_q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotting_q.append((r, c))
        
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while fresh > 0 and rotting_q:
            for _ in range(len(rotting_q)):
                r, c = rotting_q.popleft()
                for (dr, dc) in directions:
                    if self._coord_valid(r + dr, c + dc, visited, grid):
                        rotting_q.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
                        fresh -= 1
            # only after processing the current frontier should the minutes go up
            minute += 1
            
        return minute if fresh == 0 else -1
