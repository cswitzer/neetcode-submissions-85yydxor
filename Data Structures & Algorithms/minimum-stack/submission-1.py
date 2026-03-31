class MinStack:

    def __init__(self):
        # should always stay the same size, which makes it easy
        # to track the min value at every step
        self.main_stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if self.min_stack:
            min_val = min(val, self.min_stack[-1])
            self.min_stack.append(min_val)
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
