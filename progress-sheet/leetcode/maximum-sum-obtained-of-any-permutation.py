class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        n = len(nums)
        freq = [0]*(n+1)
        ans = 0

        for i in requests:
            freq[i[0]] += 1
            if i[1] < n:
                freq[i[1]+1] -= 1
        
        for i in range(1,n):
            freq[i] += freq[i-1]
        
        freq.pop()
        freq.sort()

        for i in range(n):
            ans += freq[i] * nums[i]

        return ans % (10**9+7)




    