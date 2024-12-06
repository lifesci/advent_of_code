import re

p1_total = 0
p2_total = 0
enabled = True
total_string = ""

with open("input.txt") as f:
    for line in f:
        total_string += line

raw_instructions = list(re.finditer("mul\(([0-9]{1,3}),([0-9]{1,3})\)", total_string))
dos = list(re.finditer("do\(\)", total_string))
donts = list(re.finditer("don't\(\)", total_string))

# part 1
for raw_instruction in raw_instructions:
    a = int(raw_instruction[1])
    b = int(raw_instruction[2])
    product = a*b
    p1_total += a*b

# part 2
inst_idx = 0
dos_idx = 0
donts_idx = 0

while inst_idx < len(raw_instructions):
    next_inst = raw_instructions[inst_idx]
    next_do = None if dos_idx >= len(dos) else dos[dos_idx]
    next_dont = None if donts_idx >= len(donts) else donts[donts_idx]

    if (next_do is None or next_inst.start(0) < next_do.start(0)) and (next_dont is None or next_inst.start(0) < next_dont.start(0)):
        inst_idx += 1
        if enabled:
            a = int(next_inst[1])
            b = int(next_inst[2])
            product = a*b
            p2_total += a*b
    elif next_do is not None and next_do.start(0) < next_inst.start(0) and (next_dont is None or next_do.start(0) < next_dont.start(0)):
        enabled = True
        dos_idx += 1
    else:
        enabled = False
        donts_idx += 1

print(f"Part 1 solution: {p1_total}")
print(f"Part 2 solution: {p2_total}")
