class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = deque()
        self.fullBack = False
        

    def enQueue(self, value: int) -> bool:
        if len(self.queue) == self.size:
            return False
        # if self.fullBack:
        #     self.queue.appendleft(value)
        #     return True
        self.queue.append(value)
        # if len(self.queue) == self.size:
        #     self.fullBack = True
        return True

    def deQueue(self) -> bool:
        if self.queue:
            self.queue.popleft()
            return True
        return False
    
        

    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        else:
            return -1

        

    def isEmpty(self) -> bool:
        return  not len(self.queue)
        

    def isFull(self) -> bool:
        return len(self.queue) == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()