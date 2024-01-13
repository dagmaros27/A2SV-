from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = 0
        min_diff = float('inf')
        n = len(nums)
        nums.sort()

        for i in range(n-2):
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = abs(current_sum - target)

                if current_diff < min_diff:
                    min_diff = current_diff
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
