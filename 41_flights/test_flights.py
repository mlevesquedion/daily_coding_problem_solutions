from pytest import mark


def find_path(flights, target):
    path = [target]
    while target is not None:
        for flight in flights:
            if flight[0] == target:
                path.append(flight[1])
                target = flight[1]
                break
        else:
            target = None
    return path if len(path) == len(flights) + 1 else None


def find_path(flights, start):
    if len(flights) == 1:
        return list(flights[0])
    for i, (orig, dest) in enumerate(flights):
        if orig == start:
            return [start] + find_path(flights[:i] + flights[i+1:], dest)


@mark.parametrize(
    ['flights', 'start', 'expected'],
    [
        [
            [
                ('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')
            ],
            'YUL',
            [
                'YUL', 'YYZ', 'SFO', 'HKO', 'ORD'
            ]
        ],

    ]
)
def test(flights, start, expected):
    assert find_path(flights, start) == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
