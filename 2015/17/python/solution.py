def p1_combinations(target, sizes):
    combs = 0
    for i in range(pow(2, len(sizes))):
        total = sum([size for (j, size) in enumerate(sizes) if ((i // pow(2, j)) % 2) == 1])
        if total == target:
            combs += 1
    return combs

def p2_combinations(target, sizes):
    combs = 0
    min_size = float("inf")
    for i in range(pow(2, len(sizes))):
        containers = [size for (j, size) in enumerate(sizes) if ((i // pow(2, j)) % 2) == 1]
        total = sum(containers)
        num_containers = len(containers)
        if total == target:
            if num_containers < min_size:
                min_size = num_containers
                combs = 1
            elif num_containers == min_size:
                combs += 1
    return combs

def readfile(filename):
    with open(filename) as f:
        return [int(l.strip()) for l in f]

if __name__ == "__main__":
    total = 150
    sizes = readfile("input")
    print(p1_combinations(total, sizes))
    print(p2_combinations(total, sizes))
