class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        ans = 0
        for i in range(2,len(nums)): #the loop doesnt work for forward but for backward i wonder why???
            j,k = 0, i-1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    ans += k-j
                    k -= 1
                else:
                    j += 1
        return ans

