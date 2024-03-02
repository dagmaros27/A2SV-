class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        else :
            if n % 4 != 0:
                return False
            else: 
                n = n//4
                return self.isPowerOfFour(n)
        # if n == 1: return True
        # if n < 1: return False
        # return self.isPowerOfFour(n/4)
        
        
        