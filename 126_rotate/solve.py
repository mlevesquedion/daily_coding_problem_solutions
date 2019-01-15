from quicktest import test


def rotate(arr, k):
    return arr[k:] + arr[:k]


def rotate(arr, k):
    def rotate_once():
        temp = arr[0]
        for i in range(len(arr) - 1):
            arr[i] = arr[i + 1]
        arr[-1] = temp
    for i in range(k):
        rotate_once()
    return arr


def rotate(arr, k):
    k = k % len(arr)
    temp = arr[:k]
    for i in range(len(arr) - k):
        arr[i] = arr[i + k]
    arr_pos = len(arr) - k
    for x in temp:
        arr[arr_pos] = x
        arr_pos += 1
    return arr


if __name__ == "__main__":
    test(
        rotate,
        [
            [[1, 2, 3, 4], 0, [1, 2, 3, 4]],
            [[1, 2, 3, 4], 1, [2, 3, 4, 1]],
            [[1, 2, 3, 4], 4, [1, 2, 3, 4]],
            [[5, 4, 3, 2, 1], 2, [3, 2, 1, 5, 4]]
        ]
    )
