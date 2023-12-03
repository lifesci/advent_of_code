from itertools import dropwhile

DIGITS = {str(i): i for i in range(10)}
DIGITS["one"] = 1
DIGITS["two"] = 2
DIGITS["three"] = 3
DIGITS["four"] = 4
DIGITS["five"] = 5
DIGITS["six"] = 6
DIGITS["seven"] = 7
DIGITS["eight"] = 8
DIGITS["nine"] = 9

def rev(s):
    return s[::-1]

def firstDigit(s):
    return int(list(dropwhile(lambda c: c not in DIGITS, s))[0])

def calib(line):
    return firstDigit(line)*10 + firstDigit(rev(line))


def p2Calib(s):
    maxLen = 5
    acc = ""
    curDigit = None
    firstDigit = None
    for char in s:
        if char in DIGITS:
            curDigit = DIGITS[char]
            acc = ""
        else:
            if len(acc) == maxLen:
                acc = acc[1:]
            acc += char
            for key in DIGITS.keys():
                if len(key) == 1:
                    continue
                if key in acc:
                    curDigit = DIGITS[key]
        if curDigit is not None:
            if firstDigit is None:
                firstDigit = curDigit
    lastDigit = curDigit
    return firstDigit * 10 + lastDigit

with open("input") as f:
    lines = f.readlines()
    p1 = sum(
        map(
            calib,
            lines
        )
    )
    print(f"Part 1: {p1}")
    p2 = sum(
        map(
            p2Calib,
            lines
        )
    )
    print(f"Part 2: {p2}")
