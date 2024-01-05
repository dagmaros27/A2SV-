class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dic = defaultdict(int)
        l = 0
        longest = 0
        for r in range(len(s)):
            dic[s[r]] += 1

            while dic[s[r]] > 1:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1
            longest = max(longest, len(dic))
        

        return longest
            