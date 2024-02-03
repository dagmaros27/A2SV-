class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        road = [0]*1001
        maxEle = 0
        for i in trips:
            road[i[1]] += i[0]
            road[i[2]] -= i[0]
            maxEle = max([maxEle, i[1], i[2]])
        for i in range(1, maxEle):
            road[i] += road[i-1]
            if road[i] > capacity:
                return False 
        if road[0] > capacity:
            return False


        return True
        