def find_xmas(puzzle, row, col, rows, cols):
    count = 0
    possibilities = [
        [(row - 1, col), (row - 2, col), (row - 3, col)],
        [(row - 1, col + 1), (row - 2, col + 2), (row - 3, col + 3)],
        [(row, col + 1), (row, col + 2), (row, col + 3)],
        [(row + 1, col + 1), (row + 2, col + 2), (row + 3, col + 3)],
        [(row + 1, col), (row + 2, col), (row + 3, col)],
        [(row + 1, col - 1), (row + 2, col - 2), (row + 3, col - 3)],
        [(row, col - 1), (row, col - 2), (row, col - 3)],
        [(row - 1, col - 1), (row - 2, col - 2), (row - 3, col - 3)],
    ]
    for possibility in possibilities:
        skip = False
        for r, c in possibility:
            if r < 0 or r >= rows:
                skip = True
                break
            if c < 0 or c >= cols:
                skip = True
                break
        if skip:
            continue

        letters = [puzzle[r][c] for r, c in possibility]
        if letters == ['M', 'A', 'S']:
            count += 1
    return count

def find_x_mas(puzzle, row, col, rows, cols):
    if row == 0 or col == 0:
        return False
    try:
        top_left = puzzle[row - 1][col - 1]
        top_right = puzzle[row - 1][col + 1]
        bottom_left = puzzle[row + 1][col - 1]
        bottom_right = puzzle[row + 1][col + 1]
        tl_br = (
            (top_left == "M" and bottom_right == "S")
            or (top_left == "S" and bottom_right == "M")
        )
        bl_tr = (
            (bottom_left == "M" and top_right == "S")
            or (bottom_left == "S" and top_right == "M")
        )
        return tl_br and bl_tr
    except IndexError:
        return False

puzzle = []
with open("input") as raw_puzzle:
    for line in raw_puzzle:
        puzzle.append(line.strip())

rows = len(puzzle)
cols = len(puzzle[0])

row = 0

xmas_count = 0
x_mas_count = 0

while row < rows:
    col = 0
    while col < cols:
        letter = puzzle[row][col]
        if letter == 'X':
            xmas_count += find_xmas(puzzle, row, col, rows, cols)
        if letter == 'A':
            if find_x_mas(puzzle, row, col, rows, cols):
                x_mas_count += 1
        col += 1
    row += 1

print(xmas_count)
print(x_mas_count)

