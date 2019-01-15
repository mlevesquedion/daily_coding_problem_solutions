def staircase(N, ways):
    stairs = [1 if x in ways else 0 for x in range(max(ways))]
    for i in range(N):
        sum_previous = 0
        for way in ways:
            sum_previous += stairs[way-1]
        stairs.append(sum_previous)
        stairs.pop(0)
    return stairs[-1]


if __name__ == '__main__':
    N = 4
    ways = {1, 2}
    assert staircase(4, ways) == 5
