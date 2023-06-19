from dataclasses import dataclass

@dataclass
class Box:
    l: int
    w: int
    h: int

INPUT_FILE = "input"

def readfile(filename):
    with open(filename) as f:
        return [Box(*[int(val) for val in line.split("x")]) for line in f]

def areas(box):
    return (box.l*box.w, box.l*box.h, box.h*box.w)

def volume(box):
    return box.l * box.h * box.w

def ribbon_perim(box):
    return 2*min(box.l+box.w, box.l+box.h, box.w+box.h)

def ribbon_len(box):
    return ribbon_perim(box) + volume(box)

def total_area(box):
    return 2*sum(areas(box)) + min(areas(box))

def p1(data):
    return sum([total_area(box) for box in data])

def p2(data):
    return sum([ribbon_len(box) for box in data])

if __name__ == "__main__":
    data = readfile(INPUT_FILE)
    print(p1(data))
    print(p2(data))
