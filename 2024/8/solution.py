positions = {}
antinodes = set()
p2_antinodes = set()

def is_antinode_valid(antinode, rows, cols):
    row, col = antinode
    return 0 <= row < rows and 0 <= col < cols

def p2_antinodes_for_pair(start_row, start_col, d_row, d_col, rows, cols):
    antinodes = set()
    cur_row = start_row
    cur_col = start_col
    while 0 <= cur_row < rows and 0 <= cur_col < cols:
        antinodes.add((cur_row, cur_col))
        cur_row += d_row
        cur_col += d_col

    cur_row = start_row
    cur_col = start_col
    while 0 <= cur_row < rows and 0 <= cur_col < cols:
        antinodes.add((cur_row, cur_col))
        cur_row -= d_row
        cur_col -= d_col

    return antinodes

def get_antinodes(pos_list, rows, cols):
    antinodes = set()
    p2_antinodes = set()
    # compare all pairs
    primary_idx = 0
    while primary_idx < len(pos_list) - 1:
        secondary_idx = primary_idx + 1
        primary_row, primary_col = pos_list[primary_idx]
        while secondary_idx < len(pos_list):
            secondary_row, secondary_col = pos_list[secondary_idx]
            d_row = secondary_row - primary_row
            d_col = secondary_col - primary_col
            p2_antinodes = p2_antinodes | p2_antinodes_for_pair(primary_row, primary_col, d_row, d_col, rows, cols)
            antinode_1 = (secondary_row + d_row, secondary_col + d_col)
            if is_antinode_valid(antinode_1, rows, cols):
                antinodes.add(antinode_1)
            antinode_2 = (primary_row - d_row, primary_col - d_col)
            if is_antinode_valid(antinode_2, rows, cols):
                antinodes.add(antinode_2)
            secondary_idx += 1
        primary_idx += 1
    return antinodes, p2_antinodes

with open("input") as f:
    rows = 0
    cols = 0
    for line_idx, raw_line in enumerate(f):
        rows += 1
        cols = len(raw_line.strip())
        for char_idx, char in enumerate(raw_line.strip()):
            if char == '.':
                continue
            positions.setdefault(char, [])
            positions[char].append((line_idx, char_idx))

for char in positions:
    new_antinodes, new_p2_antinodes = get_antinodes(positions[char], rows, cols)
    antinodes = antinodes | new_antinodes
    p2_antinodes = p2_antinodes | new_p2_antinodes


print(f"Part 1 solution: {len(antinodes)}")
print(f"Part 2 solution: {len(p2_antinodes)}")

