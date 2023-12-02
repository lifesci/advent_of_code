def argmax(l):
    m = None
    max_i = None
    for i, e in enumerate(l):
        if m is None or e > m:
            m = e
            max_i = i
    return max_i

class Reindeer:
    def __init__(self, name, speed, time, rest):
        self.name = name
        self.speed = speed
        self.time = time
        self.rest = rest

    def fly(self, seconds):
        cycle_len = self.time + self.rest
        cycles = seconds//cycle_len
        remainder = min(self.time, seconds % cycle_len)
        seconds_flying = cycles * self.time + remainder
        return self.speed * seconds_flying

def readfile(filename):
    deers = []
    with open(filename) as f:
        for line in f:
            vals = line.strip().split(" ")
            name = vals[0]
            speed = int(vals[3])
            time = int(vals[6])
            rest = int(vals[-2])
            deers.append(Reindeer(name, speed, time, rest))
    return deers

def p1(deers, seconds):
    return max(deer.fly(seconds) for deer in deers)

def p2(deers, seconds):
    scores = {}
    for deer in deers:
        scores[deer.name] = 0

    for i in range(1, seconds + 1):
        distances = [deer.fly(i) for deer in deers]
        max_index = argmax(distances)
        best_deer = deers[max_index]
        scores[best_deer.name] += 1

    return max(scores.values())

if __name__ == "__main__":
    deers = readfile("input")
    print(p1(deers, 2503))
    print(p2(deers, 2503))
