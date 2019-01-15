from quicktest import test


class Node:

    def __init__(self, head, tail=None):
        self.head = head
        self.tail = tail

    def __str__(self):
        return f'{self.head}{" -> " + str(self.tail) if self.tail else ""}'


def to_list(number):
    return Node(number % 10, to_list(number // 10)) if number else None


def to_number(list):
    if list is None:
        return 0
    return list.head + 10 * to_number(list.tail)


def sum(list1, list2):
    return to_list(to_number(list1) + to_number(list2))


if __name__ == '__main__':
    print(sum(Node(9, Node(9)), Node(5, Node(2))))
