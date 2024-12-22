def get_neighbours(y, x):
    return [
        (y - 1, x),
        (y + 1, x),
        (y, x - 1),
        (y, x + 1),
    ]

def price_region(grid, region):
    rows = len(grid)
    cols = len(grid[0])
    area = len(region)
    perimeter = 0
    for y, x in region:
        char = grid[y][x]
        neighbours = get_neighbours(y, x)
        for n_y, n_x in neighbours:
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
        for n_y, n_x in neighbours:
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

