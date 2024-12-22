class Button:
    def __init__(self, dx, dy, name):
        self.dx = dx
        self.dy = dy
        self.name = name

    def to_str(self):
        return f'Button {self.name}: X+{self.dx}, Y+{self.dy}'

class Machine:
    def __init__(self, a, b, x, y):
        self.a = a
        self.b = b
        self.x = x
        self.y = y

    def to_str(self):
        return '\n'.join([
            self.a.to_str(),
            self.b.to_str(),
            f'Prize: X={self.x}, Y={self.y}'
        ])

def parse_button(raw_button, name):
    mods = raw_button.split(': ')[1].split(', ')
    dx = int(mods[0].split('+')[1])
    dy = int(mods[1].split('+')[1])
    return Button(dx, dy, name)

def parse_prize(raw_prize):
    raw_positions = raw_prize.split(': ')[1].split(', ')
    x = int(raw_positions[0].split('=')[1])
    y = int(raw_positions[1].split('=')[1])
    return x, y

def parse_machine(raw_machine):
    a = parse_button(raw_machine[0], "A")
    b = parse_button(raw_machine[1], "B")
    x, y = parse_prize(raw_machine[2])
    return Machine(a, b, x, y)

raw_machine_list = []

with open("test_input") as f:
    cur_lines = []
    for raw_line in f:
        line = raw_line.strip()
        if not line:
            raw_machine_list.append(cur_lines)
            cur_lines = []
        else:
            cur_lines.append(line)

machine_list = [parse_machine(m) for m in raw_machine_list]

