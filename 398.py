class Node:
    def __init__(self, succ=None):
        self.succ = succ


def solve(linked, k):
    head = linked
    end = linked
    for _ in range(k):
        end = end.succ
    while True:
        end = end.succ
        if end is None:
            break
        linked = linked.succ
    linked.succ = linked.succ.succ
    return head


linked = Node(Node(Node(Node(Node(Node(Node()))))))
k = 3

to_remove = linked.succ.succ.succ.succ
to_remove_succ = to_remove.succ
linked = solve(linked, k)

assert linked.succ.succ.succ.succ is to_remove_succ
