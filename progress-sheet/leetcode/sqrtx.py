class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 2:
            return 1
        l,h = 0, x
        while l <= h:
            m = (l+h)//2

            if m*m < x:
                l = m + 1
            else:
                h = m -1
        #edgecases
        if l == 0:
            return 0
        return l if l*l == x else l-1
        