class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        mxm, curr = 0,0

        for idx,num in enumerate(nums, start =1):
            curr += num

            avg = ceil(curr/idx)
            mxm = max(mxm, avg)
        return mxm



        
        
        


        