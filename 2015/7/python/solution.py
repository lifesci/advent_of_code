from dataclasses import dataclass
from enum import Enum

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def parseval(val):
    try:
        return int(val)
    except ValueError:
        return val

class Type(Enum):
    AND = 1
    OR = 2
    LSHIFT = 3
    RSHIFT = 4
    NOT = 5
    GATE = 6
    LITERAL = 7

class Child:
    def __init__(self, val):
        self.type = Type.LITERAL if isint(val) else Type.GATE
        self.val = parseval(val)

class Circuit:
    def __init__(self):
        self.gates = {}

    def add_gate(self, gate):
        self.gates[gate.name] = gate

    def eval_child(self, child):
        if child.type == Type.LITERAL:
            return child.val
        return self.eval(child.val)

    def eval(self, name):
        gate = self.gates[name]
        if gate.type == Type.LITERAL:
            out = gate.l.val
        elif gate.type == Type.GATE:
            out = self.eval(gate.l.val)
        elif gate.type == Type.NOT:
            out = ~self.eval_child(gate.l)
        elif gate.type == Type.AND:
            out = self.eval_child(gate.l) & self.eval_child(gate.r)
        elif gate.type == Type.OR:
            out = self.eval_child(gate.l) | self.eval_child(gate.r)
        elif gate.type == Type.LSHIFT:
            out = self.eval_child(gate.l) << self.eval_child(gate.r)
        elif gate.type == Type.RSHIFT:
            out = self.eval_child(gate.l) >> self.eval_child(gate.r)

        self.gates[name].type = Type.LITERAL
        self.gates[name].l = Child(out)
        return out

    def p2_eval(self, name, override_gate, override_val):
        b = self.gates[override_gate]
        b.type = Type.LITERAL
        b.l.val = override_val
        return self.eval(name)

class Gate:
    typemap = {
        "AND": Type.AND,
        "OR": Type.OR,
        "RSHIFT": Type.RSHIFT,
        "LSHIFT": Type.LSHIFT,
    }

    @staticmethod
    def parse(s):
        [l, r] = s.split("->")
        name = r.strip()
        inp = l.strip().split(" ")
        lchild = None
        rchild = None
        if len(inp) == 1:
            typ = Type.LITERAL if isint(inp[0]) else Type.GATE
            lchild = Child(inp[0])
        elif len(inp) == 2:
            typ = Type.NOT
            lchild = Child(inp[1])
        else:
            typ = Gate.typemap[inp[1]]
            lchild = Child(inp[0])
            rchild = Child(inp[2])
        return Gate(name, typ, lchild, rchild)

    def __init__(self, name, typ, l, r):
        self.name = name
        self.type = typ
        self.l = l
        self.r = r

def readfile(filename):
    circuit = Circuit()
    with open(filename) as f:
        for line in f:
            circuit.add_gate(Gate.parse(line.strip()))
    return circuit

if __name__ == "__main__":
    circuit = readfile("input")
    p1 = circuit.eval("a")
    print(p1)
    circuit = readfile("input")
    print(circuit.p2_eval("a", "b", p1))
