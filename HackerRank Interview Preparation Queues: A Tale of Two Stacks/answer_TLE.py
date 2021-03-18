class MyQueue(object):
    stack = list()
    tmp_stack = list()

    def __init__(self):
        self.stack = []
        self.tmp_stack = []

    def peek(self):
        while len(self.stack) > 1:
            val = self.stack.pop(-1)
            self.tmp_stack.append(val)
        last = self.stack.pop(-1)
        self.tmp_stack.append(last)

        while self.tmp_stack:
            val = self.tmp_stack.pop(-1)
            self.stack.append(val)

        self.tmp_stack = []
        return last

    def pop(self):
        while len(self.stack) > 1:
            val = self.stack.pop(-1)
            self.tmp_stack.append(val)
        last = self.stack.pop(-1)

        while self.tmp_stack:
            val = self.tmp_stack.pop(-1)
            self.stack.append(val)

        self.tmp_stack = []
        return last

    def put(self, value):
        self.stack.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())