class Solution:
    def get_treasure_positions(self, grid: List[List[int]]) -> Set[Tuple[int, int]]:
        ROWS, COLS = len(grid), len(grid[0])
        treasure_positions = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    treasure_positions.add((r, c))
        return treasure_positions

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        treasure_positions = self.get_treasure_positions(grid)
        for pos in treasure_positions:
            q = deque()
            q.append(pos)
            distance = 0
            visited = set()
            visited.add(pos)
            while q:
                q_len = len(q)
                for _ in range(q_len):
                    r, c = q.popleft()
                    visited.add((r, c))
                    grid[r][c] = min(grid[r][c], distance)

                    for dr, dc in directions:
                        coord = (r + dr, c + dc)
                        if (
                            coord not in visited and
                            0 <= coord[0] < ROWS and
                            0 <= coord[1] < COLS and
                            grid[coord[0]][coord[1]] != 0 and
                            grid[coord[0]][coord[1]] != -1
                        ):
                            q.append((r + dr, c + dc))
                distance += 1
                


