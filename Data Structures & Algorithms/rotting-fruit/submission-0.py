class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while fresh > 0 and queue:
            # queue represents nth layer of rotten oranges
            # process them all and add the next layer
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        min(row, col) < 0 or
                        row == ROWS or col == COLS or
                        (row, col) in visited or
                        grid[row][col] != 1
                    ):
                        continue
                    grid[row][col] = 2
                    queue.append((row, col))
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
