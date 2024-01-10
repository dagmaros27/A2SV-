class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        l = 0
        longest = 0
        for r in range(len(nums)):
            hmap[nums[r]] += 1
            while hmap[0] > 1:
                hmap[nums[l]] -= 1
                l += 1
            longest = max(longest, r-l)
        
        return longest
