class Solution:
    def maxScore(self, s: str) -> int:
        maxSum = 0
        total1 = s.count('1')
        zero = 1 if s[0]=='0' else 0
        one = 1 if s[0]=='1' else 0
        for i in range(1,len(s)):
            sum = zero + (total1-one)
            maxSum = max(sum,maxSum)
            if s[i] == '0':
                zero += 1
            if s[i] == '1':
                one += 1 
        
        return maxSum