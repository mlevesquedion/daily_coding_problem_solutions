def solve(arr):
    tail = head = 0
    best_tail = best_head = best_size = 0
    all_distinct = set()
    while head < len(arr):
        if arr[head] in all_distinct:
            while arr[tail] != arr[head]:
                all_distinct.remove(arr[tail])
                tail += 1
            tail, head = tail + 1, head + 1
        else:
            all_distinct.add(arr[head])
            head += 1
            if len(all_distinct) > best_size:
                best_tail, best_head = tail, head
                best_size = len(all_distinct)
    return arr[best_tail:best_head]


arr = [5, 1, 3, 5, 2, 3, 4, 1]
assert solve(arr) == [5, 2, 3, 4, 1]
