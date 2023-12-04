class Solution:
    def largestGoodInteger(self, num: str) -> str:
        hmap = defaultdict(int)

        l = 0
        m = 1
        ans = -1

        if len(num) < 3:
            return ""

        for r in range(2,len(num)):
            if num[l] == num[r] == num[m]:
                if int(num[r]) > ans :
                    ans = int(num[r])
            l += 1
            m += 1
        
        return "" if ans == -1 else str(ans)*3

        
        

