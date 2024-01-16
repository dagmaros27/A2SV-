class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.pf = [0]*self.n
        self.pf[0] = nums[0]
        for i in range(1,self.n):
            self.pf[i] = self.pf[i-1] + nums[i]
        print(self.pf)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pf[right]
        else:
            return self.pf[right] - self.pf[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)