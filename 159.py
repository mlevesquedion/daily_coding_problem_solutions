def first_recurring(s):
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)
    return None


if __name__ == "__main__":
    assert first_recurring("acbbac") == "b"
    assert first_recurring("abcdef") is None
