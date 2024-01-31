class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:


        seen=Counter()
        seen[0]=1
        sm=ans=0

        for i,val in enumerate(nums):
            sm+=val
            ans+=seen[sm-goal]
            seen[sm]+=1

        return ans


