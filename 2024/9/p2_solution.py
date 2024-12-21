class Disk:
    def __init__(self, data):
        self.data = data

    def checksum(self):
        total = 0
        pos = 0
        for segment in self.data:
            for _ in range(segment.size):
                if segment.value is not None:
                    total += segment.value*pos
                pos += 1
        return total

    def defrag(self):
        tail_idx = len(self.data) - 1
        while tail_idx > 0:
            tail = self.data[tail_idx]
            if tail.value is None or tail.moved:
                tail_idx -= 1
            else:
                head_idx = 0
                offset = 0
                while head_idx < tail_idx:
                    head = self.data[head_idx]
                    if (
                        head.value is not None
                        or head.size < tail.size
                    ):
                        head_idx += 1
                    else:
                        offset = self._swap(head_idx, tail_idx)
                        break
                tail_idx += offset - 1

    def _swap(self, head_idx, tail_idx):
        head = self.data[head_idx]
        tail = self.data[tail_idx]
        residual_size = head.size - tail.size
        offset = 0
        if residual_size > 0:
            offset = 1
            head.size = tail.size
            self.data[head_idx] = tail
            self.data[tail_idx] = head
            self.data = (
                self.data[:head_idx + 1]
                + [Segment(residual_size, None)]
                + self.data[head_idx + 1:]
            )
        else:
            self.data[head_idx] = tail
            self.data[tail_idx] = head

        return offset

    def print(self):
        for segment in self.data:
            segment.print()

    def pretty_print(self):
        out = ""
        for segment in self.data:
            char = "." if segment.value is None else str(segment.value)
            out += char*segment.size
        print(out)

    @classmethod
    def from_str(cls, string):
        data = []
        is_file = True
        file_id = 0
        for char in string:
            size = int(char)
            value = None
            if is_file:
                value = file_id
                file_id += 1
            is_file = not is_file
            segment = Segment(size, value)
            data.append(segment)
        return cls(data)

class Segment:
    def __init__(self, size, value):
        self.size = size
        self.value = value
        self.child = None
        self.moved = False

    def print(self):
        print(f"Size: {self.size}; Value: {self.value}; Moved: {self.moved}")

with open("input") as f:
    raw_input = f.read()

disk = Disk.from_str(raw_input.strip())
disk.defrag()
print(disk.checksum())

