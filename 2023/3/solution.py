DIGITS = {str(i) for i in range(10)}

def p1_check_cell(grid, row, col):
    row_min = max(row - 1, 0)
    col_min = max(col - 1, 0)
    row_max = min(row + 2, len(grid))
    col_max = min(col + 2, len(grid[0]))

    for i in range(row_min, row_max):
        for j in range(col_min, col_max):
            cell = grid[i][j]
            if cell not in DIGITS and cell != ".":
                return True
    return False

def p1(grid):
    total = 0
    cur_num = ""
    count_num = False

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            cell = row[j]
            if cell in DIGITS:
                cur_num += cell
                count_num = count_num or p1_check_cell(grid, i, j)
            elif len(cur_num) > 0:
                if count_num:
                    total += int(cur_num)
                cur_num = ""
                count_num = False

        if count_num:
            total += int(cur_num)
        cur_num = ""
        count_num = False

    if count_num:
        total += int(cur_num)

    return total

def p2_check_cell(grid, row, col):
    row_min = max(row - 1, 0)
    col_min = max(col - 1, 0)
    row_max = min(row + 2, len(grid))
    col_max = min(col + 2, len(grid[0]))

    gears = []

    for i in range(row_min, row_max):
        for j in range(col_min, col_max):
            cell = grid[i][j]
            if cell == "*":
                gears.append((i, j))
    return gears

def p2(grid):
    gear_counts = {}
    cur_num = ""
    cur_gears = []

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            cell = row[j]
            if cell in DIGITS:
                cur_num += cell
                cur_gears += p2_check_cell(grid, i, j)
            elif len(cur_num) > 0:
                for gear in cur_gears:
                    gear_counts.setdefault(gear, set())
                    gear_counts[gear].add(int(cur_num))
                cur_num = ""
                cur_gears = []

        if len(cur_num) > 0:
            for gear in cur_gears:
                gear_counts.setdefault(gear, set())
                gear_counts[gear].add(int(cur_num))
        cur_num = ""
        cur_gears = []

    if len(cur_num) > 0:
        for gear in cur_gears:
            gear_counts.setdefault(gear, set())
            gear_counts[gear].add(int(cur_num))

    total = 0
    for gear in gear_counts:
        nums = list(gear_counts[gear])
        if len(nums) == 2:
            total += nums[0] * nums[1]
    return total

with open("input") as f:
    lines = []
    for line in f:
        lines.append(line.strip())
    print(p1(lines))
    print(p2(lines))
