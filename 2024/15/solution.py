def print_warehouse(warehouse, robot, rows, cols):
    grid = []
    for i in range(rows):
        grid.append(['.']*cols)

    grid[robot[0]][robot[1]] = '@'
    for row, col in warehouse:
        val = warehouse[(row, col)]
        if val == 'wall':
            grid[row][col] = '#'
        else:
            grid[row][col] = 'O'
    for row in grid:
        print(''.join(row))
    print()

def print_p2_warehouse(warehouse, robot, rows, cols):
    grid = []
    for i in range(rows):
        grid.append(['.']*cols)

    grid[robot[0]][robot[1]] = '@'
    for row, col in warehouse:
        val = warehouse[(row, col)]
        if val == 'wall':
            grid[row][col] = '#'
        elif val == 'l_crate':
            grid[row][col] = '['
        elif val == 'r_crate':
            grid[row][col] = ']'
    for row in grid:
        print(''.join(row))
    print()

def add(t0, t1):
    return (t0[0] + t1[0], t0[1] + t1[1])

def execute_move(warehouse, robot, rows, cols, move):
    if move == '^':
        diff = (-1, 0)
    elif move == '>':
        diff = (0, 1)
    elif move == '<':
        diff = (0, -1)
    else:
        diff = (1, 0)
    to_move = set()
    next_coord = add(robot, diff)
    next_val = warehouse.get(next_coord)
    while next_val is not None:
        if next_val == 'wall':
            return warehouse, robot
        else:
            to_move.add(next_coord)
            next_coord = add(next_coord, diff)
            next_val = warehouse.get(next_coord)

    robot = add(robot, diff)
    new_warehouse = {}
    for coord in warehouse:
        if coord in to_move:
            new_warehouse[add(coord, diff)] = warehouse[coord]
        else:
            new_warehouse[coord] = warehouse[coord]
    return new_warehouse, robot

def execute_p2_move(warehouse, robot, rows, cols, move):
    if move == '^':
        diff = (-1, 0)
    elif move == '>':
        diff = (0, 1)
    elif move == '<':
        diff = (0, -1)
    else:
        diff = (1, 0)
    to_move = set()
    queue = [add(robot, diff)]

    while queue:
        cur_coord = queue.pop(0)
        cur_val = warehouse.get(cur_coord)
        if cur_val == 'wall':
            return warehouse, robot
        elif cur_val == 'l_crate':
            neighbour = add(cur_coord, (0, 1))
            to_move.add(cur_coord)
            to_move.add(neighbour)
            if diff[0] == 0:
                queue.append(add(neighbour, diff))
            else:
                queue.append(add(cur_coord, diff))
                queue.append(add(neighbour, diff))
        elif cur_val == 'r_crate':
            neighbour = add(cur_coord, (0, -1))
            to_move.add(cur_coord)
            to_move.add(neighbour)
            if diff[0] == 0:
                queue.append(add(neighbour, diff))
            else:
                queue.append(add(cur_coord, diff))
                queue.append(add(neighbour, diff))

    robot = add(robot, diff)
    new_warehouse = {}
    for coord in warehouse:
        if coord in to_move:
            new_warehouse[add(coord, diff)] = warehouse[coord]
        else:
            new_warehouse[coord] = warehouse[coord]
    return new_warehouse, robot


def get_p2_input(warehouse, robot, rows, cols):
    p2_rows = rows
    p2_cols = 2*cols
    p2_robot = (robot[0], robot[1]*2)
    p2_warehouse = {}
    for coord in warehouse:
        new_coord = (coord[0], coord[1]*2)
        neighbour = add(new_coord, (0, 1))
        val = warehouse[coord]
        if val == 'wall':
            p2_warehouse[new_coord] = 'wall'
            p2_warehouse[neighbour] = 'wall'
        if val == 'crate':
            p2_warehouse[new_coord] = 'l_crate'
            p2_warehouse[neighbour] = 'r_crate'
    return p2_warehouse, p2_robot, p2_rows, p2_cols

def p2(warehouse, robot, rows, cols, moves):
    # print_p2_warehouse(warehouse, robot, rows, cols)
    for move in moves:
        warehouse, robot = execute_p2_move(warehouse, robot, rows, cols, move)
        # print(move)
        # print_p2_warehouse(warehouse, robot, rows, cols)

    score = 0
    for coord in warehouse:
        if warehouse[coord] == 'l_crate':
            score += 100*coord[0] + coord[1]
    return score

def p1(warehouse, robot, rows, cols, moves):
    # print_warehouse(warehouse, robot, rows, cols)
    for move in moves:
        warehouse, robot = execute_move(warehouse, robot, rows, cols, move)
        # print(move)
        # print_warehouse(warehouse, robot, rows, cols

    score = 0
    for coord in warehouse:
        if warehouse[coord] == 'crate':
            score += 100*coord[0] + coord[1]
    return score

reading_directions = False

warehouse = {}
moves = ""

with open("input") as f:
    row = 0
    for raw_line in f:
        line = raw_line.strip()
        if not line:
            reading_directions = True
            continue
        if not reading_directions:
            cols = len(line)
            for col, char in enumerate(line):
                if char == '@':
                    robot = (row, col)
                    continue
                elif char == '.':
                    continue
                elif char == '#':
                    val = 'wall'
                elif char == 'O':
                    val = 'crate'
                key = (row, col)
                warehouse[key] = val
            row += 1
        else:
            moves += line

print(p1(warehouse, robot, row, cols, moves))
print(p2(*get_p2_input(warehouse, robot, row, cols), moves))

