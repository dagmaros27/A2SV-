class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        #split the string and recurse if you find a character that doesnt have the other case
        setter = set(s)
        for i in range(len(s)):
            if s[i].swapcase() not in setter:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return max(left,right,key=len)
        return s

            
        