import json

def readfile(filename):
    with open(filename) as f:
        return json.loads(f.readline().strip())

def numbers(data, ignore_red=False):
    t = type(data)
    if t is dict:
        if ignore_red and "red" in data.values():
            return 0
        return sum(numbers(data[key], ignore_red) for key in data)
    elif t is list:
        return sum(numbers(e, ignore_red) for e in data)
    elif t is int:
        return data
    return 0

if __name__ == "__main__":
    data = readfile("input")
    print(numbers(data))
    print(numbers(data, ignore_red=True))
