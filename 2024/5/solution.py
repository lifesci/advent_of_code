viewing_rules = True

reqs = set()

total = 0

with open("input") as f:
    for raw_line in f:
        line = raw_line.strip()
        if not line:
            viewing_rules = False
            continue

        if viewing_rules:
            before, after = line.split("|")
            reqs.add((before, after))
        else:
            pages = line.split(",")
            position_map = {}
            for i, page in enumerate(pages):
                position_map[page] = i

            is_valid = True
            for before, after in reqs:
                if before in position_map and after in position_map:
                    if position_map[before] >= position_map[after]:
                        is_valid = False
                        break

            if is_valid:
                total += int(pages[len(pages)//2])
print(total)
