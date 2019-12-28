def solve(intervals):
    deltas = [x for (beg, end) in intervals for x in ((beg, 1), (end, -1))]
    max_rooms = current_rooms = 0
    for (_, d) in sorted(deltas):
        current_rooms += d
        max_rooms = max(max_rooms, current_rooms)
    return max_rooms


assert solve([(30, 75), (0, 50), (60, 150)]) == 2
