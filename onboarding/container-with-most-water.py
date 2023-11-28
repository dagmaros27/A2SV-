class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        front,back = 0, len(height)-1
        while front < back:
            volume = (back - front) * min(height[front], height[back])
            if volume > ans:
                ans = volume
            elif height[front] < height[back]:
                front += 1
            else:
                back -=1
        return ans


            