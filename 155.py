from collections import Counter


def majority_element(arr):
    # Naive, O(n) time, O(n) space
    counts = Counter(arr)
    return counts.most_common(1)[0][0]


def majority_element(arr):
    # Boyer-Moore, O(n) time, O(1) space
    el = arr[0]
    count = 1
    for x in arr[1:]:
        if x == el:
            count += 1
        else:
            count -= 1
            if count == 0:
                el = x
                count = 1
    return el


if __name__ == "__main__":
    assert majority_element([1]) == 1
    assert majority_element([1, 1, 1, 2, 3]) == 1
    assert majority_element([2, 8, 2, 2, 3, 2, 5, 2]) == 2
