class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros = 0
        ans = 0
        for r in range(len(s)-1,-1,-1):
            if s[r] == '0':
                zeros += 1
            if s[r] == '1':
                ans += zeros
        return ans
