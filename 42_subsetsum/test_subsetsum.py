from pytest import mark


def subset_sum(S, k):
    if not S:
        return None
    if k == 0:
        return []
    first, *rest = S
    if rest:
        without_first = subset_sum(rest, k)
        with_first = subset_sum(rest, k - first)
    if without_first is not None:
        return without_first
    if with_first is not None:
        return [first] + without_first
    return None


@mark.parametrize(
    ['S', 'k', 'expected'],
    [
        [
            [12, 1, 61, 5, 9, 2], 24, [12, 9, 2, 1]
        ]
    ]
)
def test(S, k, expected):
    assert subset_sum(S, k) == expected
