class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        n = len(s)
        hmap = defaultdict(int)
        longest = 0
        for r in range(n):
            hmap[s[r]] += 1

            while r-l+1 - max(hmap.values()) > k:
                hmap[s[l]] -= 1
                l += 1
            
            longest = max(longest, r-l+1)

        return longest