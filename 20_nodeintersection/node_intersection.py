class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'Node({self.value}, {self.next})'

    def __eq__(self, other):
        return self.value == other.value


class List:

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):
        current = self.root
        while current is not None:
            yield current
            current = current.next

    def __bool__(self):
        return bool(self.root)

    def peek(self):
        if not self:
            raise ValueError("Peek from empty list")
        return self.root.value

    def pop(self):
        if not self:
            raise ValueError("Pop from empty list")
        popped = self.root.value
        self.root = self.root.next
        return popped

    def push(self, value):
        new = Node(value, self.root)
        self.root = new

    def __str__(self):
        return str(self.root)


"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""


def find_intersection(L1, L2):
    L1 = reverse(L1)
    L2 = reverse(L2)
    for x, y in zip(L1, L2):
        print(x, y)
        if x.next != y.next:
            return x


def reverse(L):
    reversed_ = List()
    while L:
        reversed_.push(L.pop())
    return reversed_


if __name__ == '__main__':
    L1 = List(Node(3, Node(7, Node(8, Node(10)))))
    L2 = List(Node(99, Node(1, Node(8, Node(10)))))
    print(find_intersection(L1, L2).value)
