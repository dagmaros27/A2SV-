class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.q1 = True

    def push(self, x: int) -> None:
        if self.q1:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self) -> int:
        if self.q1:
            while len(self.queue1) > 1:
                a = self.queue1.popleft()
                self.queue2.append(a)
            self.q1 = False
            return self.queue1.popleft()
        else:
            while len(self.queue2) > 1:
                a = self.queue2.popleft()
                self.queue1.append(a)
            self.q1 = True
            return self.queue2.popleft()
    def top(self) -> int:
        if self.q1:
            return self.queue1[-1]
        else:
            return self.queue2[-1]   
    def empty(self) -> bool:
        if self.q1:
            return len(self.queue1) ==0
        else:
            return len(self.queue2)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()