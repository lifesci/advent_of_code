def get_neighbours(y, x):
    return [
        (y - 1, x, 'top'),
        (y + 1, x, 'bottom'),
        (y, x - 1, 'left'),
        (y, x + 1, 'right'),
    ]

def price_region(grid, region):
    rows = len(grid)
    cols = len(grid[0])
    area = len(region)
    perimeter = 0
    for y, x in region:
        char = grid[y][x]
        neighbours = get_neighbours(y, x)
        for n_y, n_x, _ in neighbours:
            if (
                n_y < 0 or n_y >= rows
                or n_x < 0 or n_x >= cols
                or grid[n_y][n_x] != char
            ):
                perimeter += 1

    return area * perimeter

def price_regions(grid, regions):
    price = 0
    for region in regions:
        price += price_region(grid, region)
    return price

def get_side(grid, region, y, x, pos, char):
    rows = len(grid)
    cols = len(grid[0])
    side = set()
    if pos == 'left':
        for mod in [1, -1]:
            cur_y = y
            cur_x = x
            while (
                0 <= cur_y < rows
                and grid[cur_y][cur_x] == char
                and (
                    cur_x == 0
                    or grid[cur_y][cur_x - 1] != char
                )
            ):
                side.add((cur_y, cur_x, pos))
                cur_y += mod

    elif pos == 'right':
        for mod in [1, -1]:
            cur_y = y
            cur_x = x
            while (
                0 <= cur_y < rows
                and grid[cur_y][cur_x] == char
                and (
                    cur_x == cols - 1
                    or grid[cur_y][cur_x + 1] != char
                )
            ):
                side.add((cur_y, cur_x, pos))
                cur_y += mod

    elif pos == 'top':
        for mod in [1, -1]:
            cur_y = y
            cur_x = x
            while (
                0 <= cur_x < cols
                and grid[cur_y][cur_x] == char
                and (
                    cur_y == 0
                    or grid[cur_y - 1][cur_x] != char
                )
            ):
                side.add((cur_y, cur_x, pos))
                cur_x += mod

    elif pos == 'bottom':
        for mod in [1, -1]:
            cur_y = y
            cur_x = x
            while (
                0 <= cur_x < cols
                and grid[cur_y][cur_x] == char
                and (
                    cur_y == rows - 1
                    or grid[cur_y + 1][cur_x] != char
                )
            ):
                side.add((cur_y, cur_x, pos))
                cur_x += mod

    return side

def price_region_by_sides(grid, region):
    rows = len(grid)
    cols = len(grid[0])
    area = len(region)
    sides = 0
    checked = set()
    for y, x in region:
        char = grid[y][x]
        neighbours = get_neighbours(y, x)
        for n_y, n_x, pos in neighbours:
            if (
                n_y < 0 or n_y >= rows
                or n_x < 0 or n_x >= cols
                or grid[n_y][n_x] != char
            ):
                if (y, x, pos) in checked:
                    continue
                sides += 1
                side = get_side(grid, region, y, x, pos, char)
                checked = checked.union(side)
    return area * sides

def price_regions_by_sides(grid, regions):
    price = 0
    for region in regions:
        price += price_region_by_sides(grid, region)
    return price

def build_region(grid, y, x):
    rows = len(grid)
    cols = len(grid[0])
    region = set()
    region.add((y, x))
    char = grid[y][x]
    queue = [(y, x)]
    while len(queue):
        cur_y, cur_x = queue.pop(0)
        neighbours = get_neighbours(cur_y, cur_x)
        for n_y, n_x, _ in neighbours:
            if (
                (n_y, n_x) not in region
                and 0 <= n_y < rows
                and 0 <= n_x < cols
                and grid[n_y][n_x] == char
            ):
                region.add((n_y, n_x))
                queue.append((n_y, n_x))

    return region

def build_regions(grid):
    seen = set()
    regions = []
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if (y, x) not in seen:
                region = build_region(grid, y, x)
                seen = seen.union(region)
                regions.append(region)

    return regions

grid = []
with open("input") as f:
    for raw_line in f:
        grid.append(list(raw_line.strip()))

regions = build_regions(grid)

print(price_regions(grid, regions))
print(price_regions_by_sides(grid, regions))

