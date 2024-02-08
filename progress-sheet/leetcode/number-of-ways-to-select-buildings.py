class Solution:
    def numberOfWays(self, s: str) -> int:
        lefts = [0]*len(s)
        rights = [0]*len(s)
        zeros = 1 if s[0] == '0' else 0
        ones = 1 if s[0] == '1' else 0
        for i in range(1,len(s)):
            if s[i] == '0':
                lefts[i] = ones
                zeros += 1
            else:
                lefts[i] = zeros
                ones += 1
        zeros = 1 if s[len(s)-1] == '0' else 0
        ones = 1 if s[len(s)-1] == '1' else 0
        for i in range(len(s)-2,-1,-1):
            if s[i] == '0':
                rights[i] = ones
                zeros += 1
            else:
                rights[i] = zeros
                ones += 1
        total = 0

        for i in range(len(s)):
            if lefts[i] != 0 and rights[i] != 0:
                total += lefts[i] * rights[i]
        return total

        