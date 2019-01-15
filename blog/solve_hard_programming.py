def merge(A, B):
    result = []
    while A and B:
        if A[0] < B[0]:
            result.append(A[0])
            A = A[1:]
        else:
            result.append(B[0])
            B = B[1:]
    if not A:
        result += B
    else:
        result += A
    return result


def merge_all(lists):
    while len(lists) > 1:
        lists.append(merge(lists.pop(), lists.pop()))
    return lists.pop()


if __name__ == '__main__':
    lists = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
    expected = [10, 12, 15, 15, 17, 20, 20, 30, 32]
    assert merge_all(lists) == expected
