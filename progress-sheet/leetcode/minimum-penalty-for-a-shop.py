class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y = [0]* (len(customers)+1)
        n = [0]* (len(customers)+1)

        for i in range(1,len(y)):
            if customers[i-1] == 'Y':
                y[i-1] = 1
            else:
                n[i] = 1
        for i in range(1,len(y)):
            y[len(y)-i-1] += y[len(y)-i]
            n[i] += n[i-1]
        
        minm = float('inf')
        ans = 0
        for  i in range(len(y)):
            if minm >  n[i]+y[i]:
                ans = i
                minm = n[i]+y[i]
        return ans