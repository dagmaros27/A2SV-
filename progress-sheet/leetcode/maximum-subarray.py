
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        ss = []

        for i in nums:
            s += i
            ss.append(s)
            if s<0:
                s = 0
        print(ss)
        return max(ss)