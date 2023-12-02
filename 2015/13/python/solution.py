def permute(l):
    permutations = [[]]
    for loc in l:
        new = []
        for p in permutations:
            for i in range(len(p) + 1):
                new.append(p[:i] + [loc] + p[i:])
        permutations = new
    return permutations

def readfile(filename):
    names = set()
    scores = {}
    with open(filename) as f:
        for raw_line in f:
            line = raw_line.strip()[:-1]
            vals = line.split()
            src = vals[0]
            dst = vals[-1]
            val = int(vals[3])
            if "lose" in vals:
                val = -val
            names.add(src)
            names.add(dst)
            scores[(src, dst)] = val
    return list(names), scores

def p1(names, scores):
    highest = 0
    for p in permute(names):
        total = 0
        for i in range(len(p)):
            j = (i + 1) % len(p)
            src = p[i]
            dst = p[j]
            total += scores[(src, dst)]
            total += scores[(dst, src)]
        highest = max(highest, total)
    return highest

def p2(names, scores):
    me = "me"
    for name in names:
        scores[(me, name)] = 0
        scores[(name, me)] = 0
    names.append(me)
    return p1(names, scores)

if __name__ == "__main__":
    names, scores = readfile("input")
    print(p1(names, scores))
    print(p2(names, scores))
