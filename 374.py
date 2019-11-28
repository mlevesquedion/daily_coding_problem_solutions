# Assuming the array is strictly increasing
def solve(arr):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == mid:
            high = mid
        elif arr[mid] < mid:
            low = mid + 1
        else:  # arr[mid] > mid
            high = mid - 1
    return arr[low]


print(solve([-5, -3, 2, 3]))
