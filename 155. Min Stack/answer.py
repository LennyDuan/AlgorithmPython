class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min) == 0 or x <= self.min[-1]:
            self.min.append(x)

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop == self.min[-1]:
            self.min.pop()
        return pop

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()