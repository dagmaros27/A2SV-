class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
            
            hmap = defaultdict(int)

            l = 0
            max_len = 0
            for r in range(len(nums)):
                hmap[nums[r]] += 1
                if hmap[0] > k:
                    hmap[nums[l]] -= 1
                    l += 1
                
                max_len = max(max_len, r-l+1)
            
            return max_len
