class MyQueue(object):
    stack = list()
    tmp_stack = list()

    def __init__(self):
        self.stack = []
        self.tmp_stack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop(-1)

    def put(self, value):
        while self.stack:
            val = self.stack.pop(-1)
            self.tmp_stack.append(val)
        self.tmp_stack.append(value)

        while self.tmp_stack:
            val = self.tmp_stack.pop(-1)
            self.stack.append(val)

        # self.stack.insert(0, value)


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