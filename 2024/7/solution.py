def possibly_true(result, values):
    for i in range(pow(2, len(values) - 1)):
        test_result = values[0]
        for j in range(1, len(values)):
            value = values[j]
            should_add = (i // pow(2, j - 1)) % 2
            if should_add:
                test_result = test_result + value
            else:
                test_result = test_result * value
        if test_result == result:
            return True

    return False

p1_solution = 0

with open("input") as f:
    for raw_line in f:
        raw_result, raw_values = raw_line.strip().split(": ")
        result = int(raw_result)
        values = [int(value) for value in raw_values.split(" ")]
        if possibly_true(result, values):
            p1_solution += result

print(f"Part 1 solution: {p1_solution}")

