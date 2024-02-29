class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        arr = []
        stk = []
        mnm = inf
        for i in range(len(nums)):

            mnm = min(nums[i], mnm)

            arr.append([nums[i], mnm])
        print(arr)
        for i in range(len(arr)):
            while stk and stk[-1][0] <= arr[i][0]:
                stk.pop()
            if stk and stk[-1][1] < arr[i][0]:
                print(stk)
                return True
            stk.append(arr[i])
        
        return False

        