from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.mins = deque()
        self.stack.append(float('inf'))
        self.mins.append(float('inf'))
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.mins[-1]:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])
    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
