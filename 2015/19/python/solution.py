from dataclasses import dataclass

def parse(s):
    atoms = []
    cur_atom = None
    for char in s:
        if char == char.lower():
            cur_atom += char
        else:
            if cur_atom:
                atoms.append(cur_atom)
            cur_atom = char
    if cur_atom:
        atoms.append(cur_atom)
    return atoms

def readfile(filename):
    rules = {}
    with open(filename) as f:
        line = f.readline().strip()
        while line:
            l, r = line.split(" => ")
            rules.setdefault(l, [])
            rules[l].append(parse(r))
            line = f.readline().strip()

        compound = parse(f.readline().strip())

    return rules, compound

def p1(rules, compound):
    compounds = set()
    for i, atom in enumerate(compound):
        for rule in rules.get(atom, []):
            new_compound = compound[:i] + rule + compound[i+1:]
            compounds.add("".join(new_compound))
    return len(compounds)

def apply_rule(rule, compound, index):
    return compound[:index] + rule + compound[index+1:]

@dataclass
class BfsNode:
    compound: str
    distance: int

def p2(rules, compound):
    nodes = [BfsNode(["e"], 0)]
    while nodes:
        node = nodes.pop(0)
        if node.compound == compound:
            return node.distance
        if len(node.compound) >= len(compound):
            continue
        for i, atom in enumerate(node.compound):
            for rule in rules.get(atom, []):
                new_compound = apply_rule(rule, node.compound, i)
                nodes.append(BfsNode(new_compound, node.distance + 1))

if __name__ == "__main__":
    rules, compound = readfile("input")
    print(p1(rules, compound))
    print(p2(rules, compound))
