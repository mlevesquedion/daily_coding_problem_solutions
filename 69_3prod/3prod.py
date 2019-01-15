def three_prod(arr):
    greatest = max(arr)
    arr.remove(greatest)
    negatives = list(filter(lambda x: x < 0, arr))
    positives = list(filter(lambda x: x >= 0, arr))
    smallest_negative = None
    second_smallest_negative = None
    largest_positive = None
    second_largest_positive = None
    if negatives:
        smallest_negative = min(negatives)
        negatives.remove(smallest_negative)
        if negatives:
            second_smallest_negative = min(negatives)
            negatives.remove(second_smallest_negative)
    if positives:
        largest_positive = max(positives)
        positives.remove(largest_positive)
        if positives:
            second_largest_positive = max(positives)
            positives.remove(second_largest_positive)
    return greatest * max(
        smallest_negative *
        second_smallest_negative if smallest_negative and second_smallest_negative else float(
            '-inf'),
        largest_positive *
        second_largest_positive if largest_positive and second_largest_positive else float(
            '-inf')
    )


if __name__ == '__main__':
    arr = [-10, -10, 5, 2]
    print(three_prod(arr))
