class RecentCounter:

    def __init__(self):
        self.queue = []
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        mnm = t- 3000
        counter = 0
        for i in self.queue:
            if mnm <= i <= t:
                counter += 1
        return counter 

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)