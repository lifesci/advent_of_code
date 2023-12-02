def readfile(filename):
    paths = {}
    locs = set()
    with open(filename) as f:
        for line in f:
            (l, r) = line.strip().split(" = ")
            dist = int(r)
            (a, b) = l.split(" to ")
            locs.add(a)
            locs.add(b)
            paths[(a, b)] = dist
    return paths, tuple(locs)

def permute(l):
    permutations = [[]]
    for loc in l:
        new = []
        for p in permutations:
            for i in range(len(p) + 1):
                new.append(p[:i] + [loc] + p[i:])
        permutations = new
    return permutations

def distance(paths, path):
    dist = 0
    for i in range(len(path) - 1):
        loc = path[i]
        next_loc = path[i + 1]
        key0 = (loc, next_loc)
        key1 = (next_loc, loc)
        key = key0 if key0 in paths else key1
        dist += paths[key]
    return dist

def p1(paths, locs):
    permutations = permute(locs)
    return min(distance(paths, p) for p in permutations)

def p2(paths, locs):
    permutations = permute(locs)
    return max(distance(paths, p) for p in permutations)

if __name__ == "__main__":
    paths, locs = readfile("input")
    print(p1(paths, locs))
    print(p2(paths, locs))
