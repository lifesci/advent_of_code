def readfile(filename):
    sues = []
    with open(filename) as f:
        for raw_line in f:
            sue = {}
            line = raw_line[raw_line.index(":") + 2:]
            raw_props = line.split(", ")
            for raw_prop in raw_props:
                (name, str_val) = raw_prop.split(": ")
                sue[name] = int(str_val)
            sues.append(sue)
    return sues

def p1_match(desc, sue):
    for key in sue:
        if sue[key] != desc[key]:
            return False
    return True

def p1(desc, sues):
    for i, sue in enumerate(sues):
        if p1_match(desc, sue):
            return i + 1

def p2_match(desc, sue):
    for key in sue:
        if key in {"cats", "trees"}:
            if sue[key] <= desc[key]:
                return False
        elif key in {"pomeranians", "goldfish"}:
            if sue[key] >= desc[key]:
                return False
        elif sue[key] != desc[key]:
            return False
    return True

def p2(desc, sues):
    for i, sue in enumerate(sues):
        if p2_match(desc, sue):
            return i + 1

if __name__ == "__main__":
    desc = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    sues = readfile("input")
    print(p1(desc, sues))
    print(p2(desc, sues))
