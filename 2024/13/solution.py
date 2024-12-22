class Button:
    def __init__(self, dx, dy, name):
        self.dx = dx
        self.dy = dy
        self.name = name
        self.cost = 3 if name == "A" else 1
        self.non_zero = dx > 0 or dy > 0

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

    def p2_machine(self):
        offset = 10000000000000
        return Machine(
            self.a, self.b, self.x + offset, self.y + offset
        )

def is_inline(button, x, y):
    return (
        button.non_zero
        and x % button.dx == 0
        and y % button.dy == 0
        and x // button.dx == y // button.dy
    )

def solve_machine(machine):
    try:
        num = machine.x - machine.y*machine.b.dx/machine.b.dy
        den = machine.a.dx - machine.a.dy*machine.b.dx/machine.b.dy

        n_a = round(num/den)
        n_b = round((machine.y - n_a*machine.a.dy)/machine.b.dy)
        x_result = n_a*machine.a.dx + n_b*machine.b.dx
        y_result = n_a*machine.a.dy + n_b*machine.b.dy
        if x_result == machine.x and y_result == machine.y:
            return n_a*machine.a.cost + n_b*machine.b.cost
        return 0
    except ZeroDivisionError:
        return 0

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

def p1(machine_list):
    total_cost = 0
    for machine in machine_list:
        cost = solve_machine(machine)
        total_cost += cost
    return total_cost

def p2(machine_list):
    total_cost = 0
    updated_machine_list = [machine.p2_machine() for machine in machine_list]
    for machine in updated_machine_list:
        cost = solve_machine(machine)
        total_cost += cost
    return total_cost

raw_machine_list = []

with open("input") as f:
    cur_lines = []
    for raw_line in f:
        line = raw_line.strip()
        if not line:
            raw_machine_list.append(cur_lines)
            cur_lines = []
        else:
            cur_lines.append(line)

machine_list = [parse_machine(m) for m in raw_machine_list]

print(p1(machine_list))

print(p2(machine_list))

