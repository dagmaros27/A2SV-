class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()

        # for i in range(len(nums)+2):
        #     if i in nums:
        #         pass
        #     else:
        #         return i
        n = len(nums)
        sum = ((n)*(n+1)) // 2
        for i in nums:
          sum -= i
        
        return sum
        