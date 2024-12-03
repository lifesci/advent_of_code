def is_report_safe(report):
    diffs = []
    for i in range(1, len(report)):
        diffs.append(report[i] - report[i-1])

    is_increasing = None
    for diff in diffs:
        if abs(diff) < 1 or abs(diff) > 3:
            return False

        diff_is_inc = diff > 0
        if is_increasing is None:
            is_increasing = diff_is_inc
            continue
        elif diff_is_inc != is_increasing:
            return False
    return True


def is_report_safe_with_dampener(report):
    if is_report_safe(report):
        return True
    for i in range(len(report)):
        dampened_report = [report[j] for j in range(len(report)) if j != i]
        if is_report_safe(dampened_report):
            return True
    return False

with open("input.txt") as raw_reports:
    safe_count = 0
    safe_count_with_dampener = 0
    for raw_report in raw_reports:
        report = [int(val) for val in raw_report.strip().split()]
        if is_report_safe(report):
            safe_count += 1
        if is_report_safe_with_dampener(report):
            safe_count_with_dampener += 1

    print(f"Part 1 solution: {safe_count}")
    print(f"Part 2 solution: {safe_count_with_dampener}")

