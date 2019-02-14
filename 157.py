from collections import Counter


def any_palindrome(s):
    counts = Counter(s)
    has_odd_count = False
    for count in counts.values():
        if count % 2:
            if has_odd_count:
                return False
            has_odd_count = True
    return True


if __name__ == "__main__":
    assert any_palindrome('carrace')
    assert not any_palindrome('daily')
