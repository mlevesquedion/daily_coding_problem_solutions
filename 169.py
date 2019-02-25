class Node:

    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


def split(lst):
    left, right = None, None
    left_is_next = True
    while lst is not None:
        if left_is_next:
            left = Node(lst.val, left)
        else:
            right = Node(lst.val, right)
        lst = lst.next
        left_is_next = not left_is_next
    return left, right


def reverse(lst):
    rev = None
    while lst is not None:
        rev = Node(lst.val, rev)
        lst = lst.next
    return rev


def merge(left, right):
    lst = None
    while left is not None and right is not None:
        if left.val < right.val:
            lst = Node(left.val, lst)
            left = left.next
        else:
            lst = Node(right.val, lst)
            right = right.next
    while left is not None:
        lst = Node(left.val, lst)
        left = left.next
    while right is not None:
        lst = Node(right.val, lst)
        right = right.next
    return reverse(lst)


def solve(lst):
    if lst.next is None:
        return lst
    left, right = split(lst)
    return merge(solve(left), solve(right))


if __name__ == '__main__':
    sol = solve(Node(4, Node(1, Node(-3, Node(99)))))
    while sol is not None:
        print(sol.val)
        sol = sol.next
