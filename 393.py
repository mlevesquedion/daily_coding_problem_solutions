# O(n log n)
def solve1(numbers):
    lo, hi = 0, 0
    longest_interval = 0

    current_interval = 0
    current_lo = None

    numbers = sorted(numbers)
    for (n1, n2) in zip(numbers, numbers[1:]):
        if n1 + 1 == n2:
            current_interval += 1
            if current_lo is None:
                current_lo = n1
            if n2 - current_lo > longest_interval:
                lo, hi = current_lo, n2
                longest_interval = current_interval
        else:
            current_lo = None
            current_interval = 0
    return lo, hi


# O(n + (max - min))
def solve2(numbers):
    min_, max_ = min(numbers), max(numbers)

    all_numbers = [None for _ in range(min_, max_ + 1)]

    for n in numbers:
        all_numbers[n - min_] = n

    lo, hi = 0, 0
    longest_interval = 0
    for (n1, n2) in zip(all_numbers, all_numbers[1:]):
        if n1 is None:
            continue
        if n1 + 1 == n2:
            current_interval += 1
            if current_lo is None:
                current_lo = n1
            if n2 - current_lo > longest_interval:
                lo, hi = current_lo, n2
                longest_interval = current_interval
        else:
            current_lo = None
            current_interval = 0
    return lo, hi


input_ = [9, 6, 1, 3, 8, 10, 12, 11]
expected = (8, 12)
assert solve1(input_) == expected
assert solve2(input_) == expected
