class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.queue = deque()
        self.k = k    
        self.equals = 0
    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if len(self.queue)>self.k:
            if self.queue[0] == self.value:
                self.equals -= 1
            self.queue.popleft()
        if num == self.value:
            self.equals += 1
        return self.equals == self.k
        
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)