class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        
        target = points[0]
        arrow = 1
        print(points)
        for i in range(1,len(points)):
            if target[0] <= points[i][0] <= target[1]:
                if points[i][0] > target[0] :
                    target[0] = points[i][0]
                if points[i][1] < target[1]:
                    target[1] = points[i][1]
                
            else:
                arrow += 1
                target = points[i]
        return arrow



            

        