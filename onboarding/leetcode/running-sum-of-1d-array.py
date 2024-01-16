class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # total = 0
        # ans = []
        # for i in nums:
        #     total += i
        #     ans.append(total)

        # return ans

        ans = [0]*len(nums)
        ans[0] = nums[0]
        for i in range(1,len(nums)):
            ans[i] = ans[i-1] + nums[i]

        return ans