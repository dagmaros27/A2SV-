class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        total = sum(nums)
        pf = [0] * (n+1)
        for i in range(1, n+1):
            pf[i] = pf[i-1] + nums[i-1]
        for i in range(n):
            if pf[i] == total - pf[i+1]:
                return i
        
        return -1