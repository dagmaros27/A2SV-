class Solution:
    def canJump(self, nums: List[int]) -> bool:

        first = len(nums)-2
        last = len(nums)-1

#greedy approach

        while first >= 0:
            if first + nums[first] >= last:
                last = first
            first -= 1
        if last == 0:
            return True
        return False


        