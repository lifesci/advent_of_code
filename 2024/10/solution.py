class Guide:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def score_trailheads(self):
        score = 0
        positions = []
        for row_idx, row in enumerate(self.grid):
            for col_idx, val in enumerate(row):
                if val == 0:
                    positions.append((row_idx, col_idx))

        for position in positions:
            active = [position]
            seen = set(active)
            while len(active):
                row, col = active.pop(0)
                val = self.grid[row][col]
                if val == 9:
                    score += 1
                neighbours = [
                    (row - 1, col),
                    (row, col - 1),
                    (row, col + 1),
                    (row + 1, col)
                ]
                for row, col in neighbours:
                    if (
                        0 <= row < self.rows
                        and 0 <= col < self.cols
                        and (row, col) not in seen
                        and self.grid[row][col] == val + 1
                    ):
                        active.append((row, col))
                        seen.add((row, col))

        return score


grid = []

with open("input") as f:
    for raw_line in f:
        grid.append([int(char) for char in raw_line.strip()])

guide = Guide(grid)
print(guide.score_trailheads())
