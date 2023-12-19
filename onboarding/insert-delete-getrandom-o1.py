class RandomizedSet:

    def __init__(self):
        self.maxNum = 0
        self.arr = []
        self.hmap = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.hmap:          
            return False
        else:
            self.hmap[val] = len(self.arr)
            self.arr.append(val)
            return True
        
    def remove(self, val: int) -> bool:
        if val in self.hmap:
            self.hmap[self.arr[-1]] = self.hmap[val]
            self.arr[self.hmap[val]] = self.arr[-1]
            self.hmap.pop(val)
            self.arr.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()