NULL = "."

def checksum(decompressed):
    idx = 0
    max_idx = sum(count for name, count in decompressed if name != NULL)
    checksum = 0
    tail_idx = len(decompressed) - 1
    region_idx = 0
    while idx < max_idx:
        name, count = decompressed[region_idx]
        if name != NULL:
            for _ in range(count):
                checksum += name*idx
                idx += 1
        else:
            to_take = count
            while to_take > 0 and idx < max_idx and tail_idx > region_idx:
                tail_name, tail_count = decompressed[tail_idx]
                if tail_name == NULL or tail_count == 0:
                    tail_idx -= 1
                else:
                    checksum += idx * tail_name
                    idx += 1
                    decompressed[tail_idx] = (tail_name, tail_count - 1)
                    to_take -= 1
        region_idx += 1
    return checksum

with open("input") as f:
    disk_map = f.read().strip()

decompressed = []

is_file = True
file_name = 0
for char in disk_map:
    count = int(char)
    if is_file:
        decompressed.append((file_name, count))
        file_name += 1
    else:
        decompressed.append((NULL, count))
    is_file = not is_file

out = checksum(decompressed)
print(out)

