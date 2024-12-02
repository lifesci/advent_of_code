
def p1():
    with open('input.txt') as raw_locations:
        list1 = []
        list2 = []
        for line in raw_locations:
            loc1, loc2 = [int(val) for val in line.strip().split()]
            list1.append(loc1)
            list2.append(loc2)

        list1.sort()
        list2.sort()
        diff_list = [abs(v1 - v2) for v1, v2 in zip(list1, list2)]

        return sum(diff_list)

def p2():
    with open('input.txt') as raw_locations:
        list1 = []
        list2 = []
        for line in raw_locations:
            loc1, loc2 = [int(val) for val in line.strip().split()]
            list1.append(loc1)
            list2.append(loc2)

        counts = {}
        for i in list1:
            counts[i] = 0

        for i in list2:
            if i in counts:
                counts[i] += 1

        similarity_score = 0
        for key in counts:
            similarity_score += key*counts[key]

        return similarity_score

print(f"Part 1 solution: {p1()}")
print(f"Part 2 solution: {p2()}")

