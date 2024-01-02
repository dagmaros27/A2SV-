class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        # zero = 0
        # i = 0
        # while i < len(nums):
        #     if nums[i] != 0:
        #         break
        #     i += 1
        # if i != len(nums)-1:
        #     nums[:] = nums[i:] + nums[:i]
        #this failed

        zeros = nums.count(0)
        for i in range(zeros):
            nums.remove(0)
            nums.append(0)
