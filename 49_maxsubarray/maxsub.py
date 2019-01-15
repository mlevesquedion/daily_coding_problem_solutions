def maxsubsum(arr):
    max_sum = 0
    running_sum = 0
    for x in arr:
        if running_sum + x > 0:
            running_sum += x
            max_sum = max(max_sum, running_sum)
        else:
            running_sum = 0
    return max_sum


if __name__ == '__main__':
    arr = [34, -50, 42, 14, -5, 86]
    assert maxsubsum(arr) == 137
    arr = [-5, -1, -8]
    assert maxsubsum(arr) == 0
