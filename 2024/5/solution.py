viewing_rules = True


p1_total = 0
p2_total = 0

def order_pages(pages, reqs):
    order = []
    befores = {l for l, r in reqs}
    afters = {r for l, r in reqs}
    parents_by_page = {}
    for page in pages:
        parents_by_page[page] = set()

    for before, after in reqs:
        parents_by_page[after].add(before)

    while parents_by_page:
        to_remove = set()
        satisfied = set(order)
        for page in parents_by_page:
            if parents_by_page[page] == satisfied:
                to_remove.add(page)

        for page in to_remove:
            del parents_by_page[page]
            order.append(page)
    return order

with open("input") as f:
    reqs = set()
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
                p1_total += int(pages[len(pages)//2])
            else:
                pages_set = set(pages)
                applied_reqs = [(l, r) for l, r in reqs if l in pages_set and r in pages_set]
                order = order_pages(pages, applied_reqs)
                p2_total += int(order[len(order)//2])

print(f"Part 1 solution: {p1_total}")
print(f"Part 2 solution: {p2_total}")
