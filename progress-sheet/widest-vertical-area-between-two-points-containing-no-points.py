class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = [i[0] for i in points]

        x_points.sort()

        max_diff = 0

        for i in range(1,len(x_points)):
            max_diff = max(max_diff, x_points[i] - x_points[i-1])

        return max_diff