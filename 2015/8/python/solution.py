def readfile(filename):
    with open(filename) as f:
        return [l.strip() for l in f]

def code(s):
    return len(s)

def memory(s):
    total = len(s) - 2
    i = 0
    while i < len(s):
        char = s[i]
        if char == "\\" and s[i+1] != "x":
            total -= 1
            i += 2
        elif char == "\\" and s[i+1] == "x":
            total -= 3
            i += 4
        else:
            i += 1
    return total

def p1(strings):
    return sum([code(s) - memory(s) for s in strings])

def encode(s):
    total = len(s) + 2
    i = 0
    while i < len(s):
        char = s[i]
        if char == "\"":
            total += 1
        elif char == "\\":
            total += 1
        i += 1
    return total

def p2(strings):
    return sum([encode(s) - code(s) for s in strings])

if __name__ == "__main__":
    data = readfile("input")
    print(p1(data))
    print(p2(data))
