class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        full = capacity
        for i in range(len(plants)-1):
            full -= plants[i]
            if  full < plants[i+1]:
                steps += ((i+1)*2)
                full = capacity
        
        return steps + len(plants)
            
