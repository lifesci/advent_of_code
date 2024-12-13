positions = {}
antinodes = set()

def is_antinode_valid(antinode, rows, cols):
    row, col = antinode
    return 0 <= row < rows and 0 <= col < cols

def get_antinodes(pos_list, rows, cols):
    antinodes = set()
    # compare all pairs
    primary_idx = 0
    while primary_idx < len(pos_list) - 1:
        secondary_idx = primary_idx + 1
        primary_row, primary_col = pos_list[primary_idx]
        while secondary_idx < len(pos_list):
            secondary_row, secondary_col = pos_list[secondary_idx]
            d_row = secondary_row - primary_row
            d_col = secondary_col - primary_col
            antinode_1 = (secondary_row + d_row, secondary_col + d_col)
            if is_antinode_valid(antinode_1, rows, cols):
                antinodes.add(antinode_1)
            antinode_2 = (primary_row - d_row, primary_col - d_col)
            if is_antinode_valid(antinode_2, rows, cols):
                antinodes.add(antinode_2)
            secondary_idx += 1
        primary_idx += 1
    return antinodes

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
    antinodes = antinodes | get_antinodes(positions[char], rows, cols)

print(f"Part 1 solution: {len(antinodes)}")

