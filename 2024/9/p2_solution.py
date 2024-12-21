class Disk:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def defrag(self):
        tail = self.tail
        while tail:
            next_tail = tail.parent
            if tail.value is None or tail.moved:
                pass
            else:
                head = self.head
                while head and head != tail:
                    if head.value is not None:
                        head = head.child
                    elif head.size < tail.size:
                        head = head.child
                    else:
                        next_tail = self._swap(head, tail)
                        break
            tail.moved = True
            tail = next_tail

    @staticmethod
    def _swap(head, tail):
        new_node_size = head.size - tail.size
        new_node = None
        if new_node_size:
            new_node = Segment(new_node_size, None, tail)

        old_tail_parent = tail.parent
        old_tail_child = tail.child

        tail.parent = head.parent
        if head.parent:
            head.parent.child = tail

        if new_node is None:
            tail.child = head.child
            if head.child:
                head.child.parent = tail
        else:
            tail.child = new_node
            new_node.child = head.child
            if head.child:
                head.child.parent = new_node

        head.size = tail.size
        head.parent = old_tail_parent
        head.child = old_tail_child
        if old_tail_parent:
            old_tail_parent.child = head
        if old_tail_child:
            old_tail_child.parent = head

        return head.parent

    def print(self):
        cur_segment = self.head
        while cur_segment:
            cur_segment.print()
            cur_segment = cur_segment.child

    def pretty_print(self):
        out = ""
        cur_segment = self.head
        while cur_segment:
            char = "." if cur_segment.value is None else str(cur_segment.value)
            out += char*cur_segment.size
            cur_segment = cur_segment.child
        print(out)

    @classmethod
    def from_str(cls, string):
        is_file = True
        file_id = 0
        tail = None
        head = None
        for char in string:
            size = int(char)
            value = None
            if is_file:
                value = file_id
                file_id += 1
            is_file = not is_file
            segment = Segment(size, value, tail)
            if tail is not None:
                tail.set_child(segment)
            tail = segment
            if head is None:
                head = segment
        return cls(head, tail)

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
        print(f"Size: {self.size}; Value: {self.value}; Moved: {self.moved}")

with open("test_input") as f:
    raw_input = f.read()

disk = Disk.from_str(raw_input.strip())
disk.defrag()

