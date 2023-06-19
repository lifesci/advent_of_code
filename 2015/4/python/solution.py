import hashlib
from itertools import dropwhile, count

def read_input(filename):
    with open(filename) as f:
        return f.readline().strip()

def md5(string):
    return hashlib.md5(string.encode()).hexdigest()

def find_prefix(prefix):
    return next(dropwhile(lambda x: not md5(data + str(x)).startswith(prefix), count(1)))

def p1(data):
    return find_prefix("00000")

def p2(data):
    return find_prefix("000000")

if __name__ == "__main__":
    data = read_input("input")
    print(p1(data))
    print(p2(data))
