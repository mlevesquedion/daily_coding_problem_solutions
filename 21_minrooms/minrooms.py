def overlap(i, j):
    a1, b1 = i if i[0] < j[0] else j
    a2, b2 = j if i[0] < j[0] else i
    if b1 < a2:
        return True


def minrooms(intervals):
    if not intervals:
        return 0
    rooms = [[intervals[0]]]
    for i in intervals[1:]:
        for room in rooms:
            if all(not overlap(i, j) for j in room):
                room.append(i)
                break
        else:
            rooms.append([i])
    return len(rooms)


if __name__ == '__main__':
    intervals = [(30, 75), (0, 50), (60, 150)]
    expected = 2
    assert minrooms(intervals) == expected
