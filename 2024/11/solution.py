import math

class Stones:
    def __init__(self, stones_list):
        self.stones = {}
        for stone in stones_list:
            self.stones.setdefault(stone, 0)
            self.stones[stone] += 1
        self.original_stones = self.stones

    def blink(self):
        new_stones = {}
        for stone in self.stones:
            count = self.stones[stone]
            digits = 1 if stone == 0 else math.floor(math.log10(stone)) + 1
            if stone == 0:
                to_add = [1]
            elif digits % 2 == 0:
                divisor = int(math.pow(10, digits // 2))
                left = stone // divisor
                right = stone % divisor
                to_add = [left, right]
            else:
                to_add = [stone*2024]
            for new_stone in to_add:
                new_stones.setdefault(new_stone, 0)
                new_stones[new_stone] += count
        self.stones = new_stones

    def run(self, steps):
        self.stones = self.original_stones
        for _ in range(steps):
            self.blink()

        count = 0
        for stone in self.stones:
            count += self.stones[stone]
        return count

    def p1(self):
        return self.run(25)

    def p2(self):
        return self.run(75)

with open("input") as f:
    raw_input = f.read()

stones = Stones([int(stone) for stone in raw_input.strip().split()])

print(stones.p1())
print(stones.p2())

