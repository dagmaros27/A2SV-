class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        ans = 0

        for i in nums:
            if i-1 in nums_set: 
                continue
            seq = 0
            j = i
            while j in nums_set:
                seq += 1
                j += 1

            
            ans = max(ans, seq)
        
        return ans