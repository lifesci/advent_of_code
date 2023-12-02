from functools import reduce

def readfile(filename):
    with open(filename) as f:
        return f.readline().strip()

def look_and_say(s):
    new = ""
    prev = ""
    for c in s:
        if not prev or c == prev[0]:
            prev += c
        else:
            new += f"{len(prev)}{prev[0]}"
            prev = c
    new += f"{len(prev)}{prev[0]}"
    return new

def p1(data):
    s = data
    for i in range(40):
        s = look_and_say(s)
    return len(s)

def p2(data):
    s = data
    for i in range(50):
        s = look_and_say(s)
    return len(s)

if __name__ == "__main__":
    data = readfile("input")
    print(p1(data))
    print(p2(data))
