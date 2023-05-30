SHAPE_SCORE = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3,
}

PICKS = ("X", "Y", "Z")

def read_input(filename):
    lines = []
    with open(filename) as f:
        for raw_line in f:
            line = raw_line.strip()
            if line:
                lines.append(line.split(" "))
    return lines

def p1(lines):
    score = 0
    for other, me in lines:
        score += SHAPE_SCORE[me]
        my_val = SHAPE_SCORE[me] - 1
        other_val = SHAPE_SCORE[other] - 1
        if my_val == other_val:
            score += 3
        elif my_val == (other_val + 1) % 3:
            score += 6
    return score

def p2(lines):
    score = 0
    for other, outcome in lines:
        if outcome == "Y":
            me = PICKS[SHAPE_SCORE[other] - 1]
        elif outcome == "X":
            me = PICKS[SHAPE_SCORE[other] - 2]
        else:
            me = PICKS[(SHAPE_SCORE[other]) % 3]
        score += SHAPE_SCORE[me]
        my_val = SHAPE_SCORE[me] - 1
        other_val = SHAPE_SCORE[other] - 1
        if my_val == other_val:
            score += 3
        elif my_val == (other_val + 1) % 3:
            score += 6
    return score

filename = "input.txt"
print(p1(read_input(filename)))
print(p2(read_input(filename)))
