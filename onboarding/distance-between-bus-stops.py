class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        sum1,sum2 = 0,0
        n = len(distance)
        i=start
        while i != destination:
            sum1 += distance[i]
            i = (i + 1) % n
        
        while i != start:
            sum2 += distance[i]
            i = (i + 1) % n
        
        return min(sum1,sum2)
        



