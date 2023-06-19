from functools import reduce

VOWELS = {"a", "e", "i", "o", "u"}
BAD = {"ab", "cd", "pq", "xy"}

def read_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def p1_concat(acc, x):
    return acc[-1] + x if acc else x

def p1_evaluate(s):
    return reduce(
        lambda acc, x: (
            p1_concat(acc[0], x),
            acc[1] + (1 if x in VOWELS else 0),
            acc[2] or (acc[0] and (x == acc[0][-1])),
            acc[3] or (p1_concat(acc[0], x) in BAD),
        ),
        s,
        ("", 0, False, False)
    )

def p1_is_nice(e):
    return e[1] >= 3 and e[2] and not e[3]

def p1(data):
    return sum([p1_is_nice(p1_evaluate(s)) for s in data])

def p2_concat(acc, x):
    return acc + x if len(acc) < 3 else acc[1:] + x

def p2_evaluate(s):
    return reduce(
        lambda acc, e: (
            p2_concat(acc[0], e[1]),
            {
                **acc[1],
                **(
                    {} if len(p2_concat(acc[0], e[1])) < 2
                    else dict([(
                        p2_concat(acc[0], e[1])[-2:],
                        [e[0]] if p2_concat(acc[0], e[1])[-2:] not in acc[1]
                        else acc[1][p2_concat(acc[0], e[1])[-2:]] + [e[0]] if e[0] > acc[1][p2_concat(acc[0], e[1])[-2:]][-1] + 1
                        else acc[1][p2_concat(acc[0], e[1])[-2:]]
                    )])
                )
            },
            acc[2] or (len(p2_concat(acc[0], e[1])) > 2 and p2_concat(acc[0], e[1])[0] == p2_concat(acc[0], e[1])[2])
        ),
        enumerate(s),
        ("", {}, False)
    )

def p2_is_nice(e):
    return reduce(lambda acc, x: acc or len(x) >= 2, e[1].values(), False) and e[2]

def p2(data):
    return sum([p2_is_nice(p2_evaluate(s)) for s in data])

if __name__ == "__main__":
    data = read_input("input")
    print(p1(data))
    print(p2(data))
