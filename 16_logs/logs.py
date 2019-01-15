class Log:

    def __init__(self):
        self.log = []

    def record(self, order_id):
        self.log.append(order_id)

    def get_last(self, i):
        return self.log[len(self.log)-i]


if __name__ == '__main__':
    log = Log()
    for i in range(10):
        log.record(i)
    print(log.get_last(1))
    print(log.get_last(3))
