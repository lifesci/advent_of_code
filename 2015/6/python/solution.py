import re

ON = 0
OFF = 1
TOGGLE = 2

class Cmd:
    def __init__(self, s):
        res = re.search(r"^(toggle|turn on|turn off) ([0-9]+,[0-9]+) through ([0-9]+,[0-9]+)$", s)
        cmd = res.group(1)
        self.cmd = TOGGLE if cmd == "toggle" else (ON if cmd == "turn on" else OFF)
        self.start = [int(v) for v in res.group(2).split(",")]
        self.end = [int(v) for v in res.group(3).split(",")]

def read_input(filename):
    with open(filename) as f:
        return [Cmd(line.strip()) for line in f]

def apply_on(point, lights):
    lights.add(point)

def apply_off(point, lights):
    lights.discard(point)

def apply_toggle(point, lights):
    if point in lights:
        lights.remove(point)
    else:
        lights.add(point)

def p1(cmds):
    on = set()
    for cmd in cmds:
        func = apply_on if cmd.cmd == ON else (apply_off if cmd.cmd == OFF else apply_toggle)
        for i in range(cmd.start[0], cmd.end[0] + 1):
            for j in range(cmd.start[1], cmd.end[1] + 1):
                func((i, j), on)
    return len(on)

def adjust(point, val, lights):
    lights.setdefault(point, 0)
    lights[point] += val
    if lights[point] <= 0:
        lights.pop(point)

def p2(cmds):
    lights = {}
    for cmd in cmds:
        val = 1 if cmd.cmd == ON else (-1 if cmd.cmd == OFF else 2)
        for i in range(cmd.start[0], cmd.end[0] + 1):
            for j in range(cmd.start[1], cmd.end[1] + 1):
                adjust((i, j), val, lights)
    return sum(lights.values())

if __name__ == "__main__":
    data = read_input("input")
    print(p1(data))
    print(p2(data))
