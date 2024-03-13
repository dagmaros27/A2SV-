class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        func1 = lambda x: x > target
        func2 = lambda x: x >= target
        ans=[]

        l,r = 0 , len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if not func2(nums[mid]):
                l = mid+1
            else:
                r = mid -1
        ans.append(l)

        l,r = 0 , len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if not func1(nums[mid]):
                l = mid+1
            else:
                r = mid -1
        ans.append(l-1)
        
        

        return ans if ans[0] <= ans[1] else [-1,-1]
            


                