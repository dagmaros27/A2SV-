class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        # nums.append(n)
        # nums.sort()
        runningSum = 0
        count = 0
        i = 0
        while runningSum < n:
            if i < len(nums) and nums[i] <= runningSum + 1:
                runningSum += nums[i]
                i += 1
            else:
                runningSum += (runningSum + 1)
                count += 1

        return count