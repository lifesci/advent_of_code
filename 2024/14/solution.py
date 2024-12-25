class Robot:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self, x_max, y_max, steps):
        return Robot(
            (self.x + self.dx*steps) % x_max,
            (self.y + self.dy*steps) % y_max,
            self.dx,
            self.dy,
        )

    def get_quadrant(self, x_max, y_max):
        quadrant = 0
        if self.x < x_max//2 and self.y < y_max//2:
            quadrant = 1
        elif self.x > x_max//2 and self.y < y_max//2:
            quadrant = 2
        elif self.x < x_max//2 and self.y > y_max//2:
            quadrant = 3
        elif self.x > x_max//2 and self.y > y_max//2:
            quadrant = 4
        return quadrant

def simulate(x_max, y_max, robots, steps):
    return [r.move(x_max, y_max, steps) for r in robots]

def print_grid(x_max, y_max, robots):
    counts = {}
    for r in robots:
        pos = (r.y, r.x)
        counts.setdefault(pos, 0)
        counts[pos] += 1

    for row in range(y_max):
        row_str = ""
        for col in range(x_max):
            key = (row, col)
            if key in counts:
                row_str += '#'
            else:
                row_str += '.'
        print(row_str)

    print()
    print()

def simulate_and_check_tree(x_max, y_max, robots):
    steps = 0
    min_score = float("inf")
    while True:
        cur_score = score(x_max, y_max, robots, 0)
        min_score = min(min_score, cur_score)
        if min_score == cur_score:
            print(min_score, steps)
            print_grid(x_max, y_max, robots)
        robots = simulate(x_max, y_max, robots, 1)
        steps += 1
    return steps

def score(x_max, y_max, robots, steps):
    updated_robots = simulate(x_max, y_max, robots, steps)
    counts = [0]*5
    for r in updated_robots:
        counts[r.get_quadrant(x_max, y_max)] += 1

    score = 1
    for i in range(1, len(counts)):
        score *= counts[i]
    return score

robots = []

TEST = False
if TEST:
    FILENAME = 'test_input'
    X_MAX = 11
    Y_MAX = 7
else:
    FILENAME = 'input'
    X_MAX = 101
    Y_MAX = 103

with open(FILENAME) as f:
    for raw_line in f:
        raw_pos, raw_vel = raw_line.strip().split(' ')
        raw_x, raw_y = raw_pos.split('=')[1].split(',')
        x = int(raw_x)
        y = int(raw_y)
        raw_dx, raw_dy = raw_vel.split('=')[1].split(',')
        dx = int(raw_dx)
        dy = int(raw_dy)
        robots.append(Robot(x, y, dx, dy))


print(score(X_MAX, Y_MAX, robots, 100))
print(simulate_and_check_tree(X_MAX, Y_MAX, robots))

