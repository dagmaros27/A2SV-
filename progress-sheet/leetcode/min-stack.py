class MinStack:

    def __init__(self):
        self.normal_stk = deque()
        self.monotone_stk = deque()

        

    def push(self, val: int) -> None:
        self.normal_stk.append(val)
        if (not self.monotone_stk) or self.monotone_stk[-1] >= val:
            self.monotone_stk.append(val)



    def pop(self) -> None:
        val = self.normal_stk.pop()
        if val == self.monotone_stk[-1]:
            self.monotone_stk.pop()
        

    def top(self) -> int:
        return self.normal_stk[-1]
        

    def getMin(self) -> int:
        return self.monotone_stk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()