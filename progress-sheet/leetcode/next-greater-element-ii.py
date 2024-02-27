class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward_stk = []
        # backward_stk = []
        ans = [-1]*n

        for i in range(2*n):
            while forward_stk and nums[forward_stk[-1]] < nums[i%n]:
                ans[forward_stk.pop()] = i%n
            forward_stk.append(i%n)

        # for j in range(2*n-1,-1,-1):
        #     if backward_stk and nums[backward_stk[-1]] < nums[j%n]:
        #         if ans[backward_stk[-1]] == -1:
        #             ans[backward_stk[-1]] = j%n
        #     backward_stk.append(j%n)
        # print(ans)
        for i in range(len(ans)):
            if ans[i] != -1:
                ans[i] = nums[ans[i]]

        return ans

        