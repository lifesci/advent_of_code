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

with open('input') as f:
    for raw_line in f:
        raw_pos, raw_vel = raw_line.strip().split(' ')
        raw_x, raw_y = raw_pos.split('=')[1].split(',')
        x = int(raw_x)
        y = int(raw_y)
        raw_dx, raw_dy = raw_vel.split('=')[1].split(',')
        dx = int(raw_dx)
        dy = int(raw_dy)
        robots.append(Robot(x, y, dx, dy))

print(score(101, 103, robots, 100))

