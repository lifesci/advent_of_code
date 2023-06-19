import functools

def p1(data):
    return functools.reduce(lambda acc, x: acc + (1 if x == "(" else -1), data, 0)

def p2(data):
    pos = 0
    for i, char in enumerate(data):
        pos += 1 if char == "(" else -1
        if pos < 0:
            return i + 1
    return -1

def readfile(filename):
    with open(filename) as f:
        line = f.readline().strip()
    return line

INPUT_FILE = "input"
if __name__ == "__main__":
    input_data = readfile(INPUT_FILE)
    print(p1(input_data))
    print(p2(input_data))
