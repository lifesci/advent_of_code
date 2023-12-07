class MappingRange:
    def __init__(self, dst_start, src_start, length):
        self.src_start = src_start
        self.dst_start = dst_start
        self.length = length

    def print(self):
        print(f"src_start: {self.src_start}; dst_start: {self.dst_start}; length: {self.length}")

class Mapping:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.ranges = []

    def add_range(self, rng):
        self.ranges.append(rng)

    def map(self, value):
        for rng in self.ranges:
            if rng.src_start <= value < (rng.src_start + rng.length):
                return rng.dst_start + value - rng.src_start
        return value

    def print(self):
        print(f"{self.src} to {self.dst}")
        for rng in self.ranges:
            rng.print()

class MappingSet:
    def __init__(self, starts):
        self.mappings = {}
        self.starts = starts

    def add_mapping(self, mapping):
        self.mappings[mapping.src] = mapping

    def p1(self):
        min_location = float("inf")
        target_type = "location"
        for s in self.starts:
            cur_value = s
            cur_type = "seed"
            while cur_type != target_type:
                mapping = self.mappings[cur_type]
                cur_value = mapping.map(cur_value)
                cur_type = mapping.dst

            min_location = min(cur_value, min_location)
        return min_location

    def print(self):
        print(f"seeds: {self.starts}")
        print()
        for key in self.mappings:
            mapping = self.mappings[key]
            mapping.print()
            print()

def read_input(filename):
    title_next = False
    mapping = None
    with open(filename) as f:
        header = f.readline().strip()
        _, raw_starts = header.split(":")
        starts = [int(start) for start in raw_starts.split()]
        mappings = MappingSet(starts)
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                if mapping is not None:
                    mappings.add_mapping(mapping)
                title_next = True
                continue
            if title_next:
                # read title
                raw_title, _ = line.split()
                src, dst = raw_title.split("-to-")
                title_next = False
                mapping = Mapping(src, dst)
            else:
                # read entry
                src_start, dst_start, length = [int(x) for x in line.split()]
                mapping.add_range(MappingRange(src_start, dst_start, length))
    return mappings


mappings = read_input("input")
print(mappings.p1())
