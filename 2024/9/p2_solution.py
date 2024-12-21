class Disk:
    def __init__(self, root):
        self.root = root

    def print(self):
        cur_segment = self.root
        while cur_segment:
            cur_segment.print()
            cur_segment = cur_segment.child

    @classmethod
    def from_str(cls, string):
        is_file = True
        file_id = 0
        prev = None
        root = None
        for char in string:
            size = int(char)
            value = None
            if is_file:
                value = file_id
                file_id += 1
            is_file = not is_file
            segment = Segment(size, value, prev)
            if prev is not None:
                prev.set_child(segment)
            prev = segment
            if root is None:
                root = segment
        return cls(root)

class Segment:
    def __init__(self, size, value, parent):
        self.size = size
        self.value = value
        self.parent = parent
        self.child = None
        self.moved = False

    def set_child(self, child):
        self.child = child

    def print(self):
        print(f"Size: {self.size}; Value: {self.value}")

with open("test_input") as f:
    raw_input = f.read()

disk = Disk.from_str(raw_input.strip())
disk.print()

