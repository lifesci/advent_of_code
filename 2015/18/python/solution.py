class Cell:
    def __init__(self, on):
        self.on = on

    def transition(self, active_neighbours):
        if self.on:
            on = active_neighbours == 2 or active_neighbours == 3
        else:
            on = active_neighbours == 3

        return Cell(on)

class Grid:
    def __init__(self, str_grid):
        self.cells = []
        for i in range(len(str_grid)):
            self.cells.append([])
            for char in str_grid[i]:
                self.cells[-1].append(Cell(char == "#"))
        self.rows = len(self.cells)
        self.cols = len(self.cells[0])

    def valid_coord(self, row, col):
        valid_row = 0 <= row < self.rows
        valid_col = 0 <= col < self.cols
        return valid_row and valid_col

    def neighbours(self, row, col):
        n = []
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if not (i == row and j == col) and self.valid_coord(i, j):
                    n.append(self.cells[i][j])
        return n

    def count_active_neighbours(self, row, col):
        return sum(n.on for n in self.neighbours(row, col))

    def transition(self):
        new_cells = []
        for row in range(self.rows):
            new_cells.append([])
            for col in range(self.cols):
                active_neighbours = self.count_active_neighbours(row, col)
                new_cells[-1].append(self.cells[row][col].transition(active_neighbours))
        self.cells = new_cells

    def count_on(self):
        total = 0
        for row in self.cells:
            for cell in row:
                total += cell.on
        return total

    def turn_on_corners(self):
        self.cells[0][0].on = True
        self.cells[0][-1].on = True
        self.cells[-1][0].on = True
        self.cells[-1][-1].on = True

    def p1_count_after_transitions(self, transitions):
        for _ in range(transitions):
            self.transition()
        return self.count_on()

    def p2_count_after_transitions(self, transitions):
        self.turn_on_corners()
        for _ in range(transitions):
            self.transition()
            self.turn_on_corners()
        return self.count_on()

    def print(self):
        for row in self.cells:
            print(" ".join(["#" if cell.on else "." for cell in row]))
        print()

def readfile(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

if __name__ == "__main__":
    str_grid = readfile("input")

    p1_grid = Grid(str_grid)
    print(p1_grid.p1_count_after_transitions(100))

    p2_grid = Grid(str_grid)
    print(p2_grid.p2_count_after_transitions(100))
