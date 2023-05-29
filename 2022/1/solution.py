def read(filename):
    cals = [[]]
    with open(filename) as f:
        for raw_line in f:
            line = raw_line.strip()
            if line:
                val = int(line)
                cals[-1].append(val)
            else:
                cals.append([])
    return cals

def p1(filename):
    cals = read(filename)
    return max(map(sum, cals))

def p2(filename):
    cals = read(filename)
    return sum(sorted(map(sum, cals), reverse=True)[:3])

print(p1("input.txt"))
print(p2("input.txt"))
