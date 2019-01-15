def stocks(arr):
    first, *rest = arr
    rolling_min = first
    max_ = 0
    for x in rest:
        rolling_min = min(x, rolling_min)
        max_ = max(x - rolling_min, max_)
    return max_


if __name__ == '__main__':
    print(stocks([9, 11, 8, 5, 7, 10]))
    print(stocks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(stocks([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(stocks([1, 2]))
    print(stocks([1]))
