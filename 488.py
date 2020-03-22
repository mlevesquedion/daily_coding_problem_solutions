# Queue as a Vector that "chases its tail" with an index, except the
# Vector is made of fixed-length arrays
# In practice we would need to reset the arrays and pointers eventually,
# and the cost of each operation would be amortized O(1)
class Queue:

    def __init__(self, array_size=3):
        assert isinstance(array_size, int) and array_size >= 1, "array size must be a positive integer"
        self.array_size = array_size
        self.head = 0
        self.tail = 0
        self.arrays = []

    def dequeue(self):
        if self.head == self.tail:
            raise RuntimeError('tried to pop from empty queue')
        array, array_index = divmod(self.head, self.array_size)
        self.head += 1
        return self.arrays[array][array_index]

    def enqueue(self, value):
        array, array_index = divmod(self.tail, self.array_size)
        if array == len(self.arrays):
            self.add_array()
        self.arrays[array][array_index] = value
        self.tail += 1

    def add_array(self):
        self.arrays.append([None for _ in range(self.array_size)])



Q = Queue()

n_elems = 10

for i in range(n_elems):
    Q.enqueue(i)

for i in range(n_elems):
    print(Q.dequeue())

