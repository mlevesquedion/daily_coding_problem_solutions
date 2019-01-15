from pytest import mark


def minpal(s):
    rev = ''
    for i, c in enumerate(s):
        if rev and c == rev[-1]:
            return rev + s[i+1:]
        rev = c + rev
    return rev + s[1:]


@mark.parametrize(
    ['s', 'expected'],
    [
        ["google", "elgoogle"],
        ["race", "ecarace"]
    ]
)
def test(s, expected):
    assert expected == minpal(s)
