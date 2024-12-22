import math

class Stones:
    def __init__(self, stones):
        self.original_stones = stones
        self.stones = stones

    def blink(self):
        new_stones = []
        for stone in self.stones:
            digits = 1 if stone == 0 else max(1, int(math.ceil(math.log10(stone))))
            if stone == 0:
                new_stones.append(1)
            elif digits % 2 == 0:
                divisor = int(math.pow(10, digits // 2))
                left = stone // divisor
                right = stone % divisor
                new_stones.append(left)
                new_stones.append(right)
            else:
                new_stones.append(stone*2024)
        self.stones = new_stones

    def p1(self):
        self.stones = self.original_stones
        for _ in range(25):
            self.blink()
        return len(self.stones)

with open("input") as f:
    raw_input = f.read()

stones = Stones([int(stone) for stone in raw_input.strip().split()])

print(stones.p1())

