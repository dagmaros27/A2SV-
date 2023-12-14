class FrequencyTracker:

    def __init__(self):
        self.hmap = defaultdict(int)
        self.freqMap = defaultdict(int)
        

    def add(self, number: int) -> None:
        if number in self.hmap:
            self.freqMap[self.hmap[number]] -= 1
        self.hmap[number] += 1
        self.freqMap[self.hmap[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.hmap:
            self.freqMap[self.hmap[number]] -= 1
            self.hmap[number] -= 1
            if self.hmap[number] < 0:
                del self.hmap[number]
       
            if self.hmap[number] > 0:
                self.freqMap[self.hmap[number]] += 1 
            
        
    def hasFrequency(self, frequency: int) -> bool:
       return self.freqMap[frequency]
        


        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)