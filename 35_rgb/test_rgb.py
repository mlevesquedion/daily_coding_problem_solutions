from pytest import mark


def rgb(arr):
    r_locations = set()
    g_locations = set()
    b_locations = set()
    for i, x in enumerate(arr):
        if x == 'R':
            r_locations.add(i)
        if x == 'G':
            g_locations.add(i)
        if x == 'B':
            b_locations.add(i)
    for i, loc in enumerate(r_locations):
        if arr[i] == 'G':
            g_locations.remove(i)
            g_locations.add(loc)
        if arr[i] == 'B':
            b_locations.remove(i)
            b_locations.add(loc)
        arr[i], arr[loc] = arr[loc], arr[i]
    for i, loc in enumerate(g_locations, len(r_locations)):
        if arr[i] == 'B':
            b_locations.remove(i)
            b_locations.add(loc)
        arr[i], arr[loc] = arr[loc], arr[i]
    return arr


@mark.parametrize(
    ['arr', 'expected'],
    [
        [[], []],
        [['R'], ['R']],
        [['R', 'R'], ['R', 'R']],
        [['R', 'G', 'B'], ['R', 'G', 'B']],
        [['B', 'G', 'R'], ['R', 'G', 'B']],
        [['G', 'B', 'R'], ['R', 'G', 'B']],
        [['G', 'B', 'B', 'G', 'B', 'R'], ['R', 'G', 'G', 'B', 'B', 'B']],
        [['G', 'B', 'R', 'R', 'B', 'R', 'G'], ['R', 'R', 'R', 'G', 'G', 'B', 'B']],
        [['B', 'R', 'R', 'R', 'R', 'R', 'R', 'R'], [
            'R', 'R', 'R', 'R', 'R', 'R', 'R', 'B']]
    ]
)
def test(arr, expected):
    assert expected == rgb(arr)
