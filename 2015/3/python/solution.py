from dataclasses import dataclass
from itertools import accumulate
from functools import reduce

@dataclass
class Pos:
    x: int
    y: int

    def l(self):
        return Pos(self.x - 1, self.y)

    def r(self):
        return Pos(self.x + 1, self.y)

    def u(self):
        return Pos(self.x, self.y + 1)

    def d(self):
        return Pos(self.x, self.y - 1)

    def move(self, char):
        return (
            self.l() if char == "<"
            else self.r() if char == ">"
            else self.d() if char == "v"
            else self.u()
        )

    def __iter__(self):
        yield self.x
        yield self.y

def read_input(filename):
    with open(filename) as f:
        return f.readline().strip()

def p1(data):
    return len(
        set(
            [
                tuple(pos) for pos in accumulate(
                    data, lambda prev, char: prev.move(char), initial=Pos(0, 0)
                )
            ]
        )
    )

def flatten(l):
    return reduce(lambda acc, x: acc + list(x), l, [])

def p2(data):
    return len(set([tuple(x) for x in flatten(
        accumulate(
            zip(
                [c for (i, c) in enumerate(data) if i % 2 == 0],
                [c for (i, c) in enumerate(data) if i % 2 == 1]
            ),
            lambda prev, pair: (prev[0].move(pair[0]), prev[1].move(pair[1])),
            initial=(Pos(0, 0), Pos(0, 0))
        )
    )]))

if __name__ == "__main__":
    data = read_input("input")
    print(p1(data))
    print(p2(data))
