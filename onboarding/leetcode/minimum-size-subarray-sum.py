class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_subarr = float('inf')
        l = 0
        sum = 0
        for r in range(len(nums)):
            sum += nums[r]

            while sum >= target:
                min_subarr = min(min_subarr, r-l+1)
                sum -= nums[l]
                l += 1
        
        return 0 if min_subarr == float('inf') else min_subarr