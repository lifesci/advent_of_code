BASE = ord("a")
MAX = 26
I = ord("i") - BASE
L = ord("l") - BASE
O = ord("o") - BASE
BAD = {I, L, O}

def string_to_int(s):
    return [ord(c) - BASE for c in s]

def int_to_string(i):
    return "".join([chr(c + BASE) for c in i])

def readfile(filename):
    with open(filename) as f:
        return f.readline().strip()

def increment(pw, ind=None, reset=False):
    ind = ind or (len(pw) - 1)
    pw[ind] = (pw[ind] + 1) % MAX
    if reset:
        for i in range(ind + 1, len(pw)):
            pw[i] = 0

    if pw[ind] == 0:
        increment(pw, ind - 1)
    return pw

def check(pw):
    pairs = set()
    run = False
    for i, val in enumerate(pw):
        if val in BAD:
            increment(pw, i, reset=True)
            return check(pw)
        if i < len(pw) - 1 and pw[i] == pw[i + 1]:
            pairs.add(pw[i])
        if not run and i < len(pw) - 2:
            run = (pw[i+1] == (pw[i] + 1)) and (pw[i + 2] == (pw[i] + 2))
    return len(pairs) > 1 and run

def p1(pw):
    int_pw = string_to_int(pw)
    increment(int_pw)
    while not check(int_pw):
        increment(int_pw)
    return int_to_string(int_pw)

if __name__ == "__main__":
    data = readfile("input")
    new_pw = p1(data)
    print(new_pw)
    print(p1(new_pw))
