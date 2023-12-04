class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxlen = 0

        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
               l = r+1
            
            maxlen = max(maxlen, r-l +1)
        
        return maxlen

