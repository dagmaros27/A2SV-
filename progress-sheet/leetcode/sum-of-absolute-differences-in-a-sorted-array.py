class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        pf = [0] * (n+1)
      
        for i in range(1,n+1):
            pf[i] = pf[i-1] + nums[i-1]
        
        for  i in range(n):
            summ = nums[i]*i - (pf[i])
            summ += (pf[n]- pf[i+1]) - (nums[i]* (n-i-1))
            ans.append(summ)

        return ans 
        

        
