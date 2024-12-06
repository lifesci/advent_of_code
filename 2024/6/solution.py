
DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


def walk(start_row, start_col, lab):
    global DIRS
    dir_index = 0
    row = start_row
    col = start_col
    positions = set()
    positions_with_dirs = set()
    moved = False
    while 0 <= row < len(lab) and 0 <= col < len(lab[0]):
        if (row, col, dir_index) in positions_with_dirs:
            return None
        positions.add((row, col))
        positions_with_dirs.add((row, col, dir_index))
        dr, dc = DIRS[dir_index]
        next_row = row + dr
        next_col = col + dc
        if 0 <= next_row < len(lab) and 0 <= next_col < len(lab[0]):
            next_loc = lab[next_row][next_col]
        else:
            next_loc = "."
        if next_loc == "#":
            dir_index = (dir_index + 1) % len(DIRS)
        else:
            row = next_row
            col = next_col
    return len(positions)

lab = []
with open("input") as f:
    for line in f:
        lab.append(list(line.strip()))

    for i, row in enumerate(lab):
         for j, char in enumerate(row):
            if char == "^":
                start_row = i
                start_col = j

    print(f"Part 1 solution: {walk(start_row, start_col, lab)}")
    lab_copy = [row[:] for row in lab]

    loops = 0
    for i in range(len(lab)):
        row = lab[i]
        for j in range(len(row)):
            char = row[j]
            if char == ".":
                lab[i][j] = "#"
                if walk(start_row, start_col, lab) is None:
                    loops += 1
                lab[i][j] = "."

    print(f"Part 2 solution: {loops}")
