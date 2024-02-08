class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pf = [0]* (len(nums)+1)

        for i in range(1,len(nums)+1):
            pf[i] = pf[i-1]+ nums[i-1]

        counter = defaultdict(int)
        ans = 0
        for i in range(len(pf)):
            rem = pf[i]%k
            if rem in counter:
                ans += counter[rem] 
            counter[rem] += 1
        
        return ans


 
        