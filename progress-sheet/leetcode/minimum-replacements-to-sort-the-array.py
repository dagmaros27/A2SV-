class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        minNum = nums[-1]
        for i in range(len(nums)-2, -1,-1):
            d = ceil(nums[i]/ minNum) # the amount of numbers we divide the element, where the max possible being the minNum
            res += d - 1 #d -1 is the amount of divides we do for that certain number
            minNum = nums[i]// d # we change the minNum to the smallest of the numbers we divide the current element to
        return res
        #since it is greedy, we dont append elements we dont care about the array being sorted our goal is to make each number at most equal to the one after it
