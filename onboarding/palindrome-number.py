class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative numbers and numbers that end with 0 can't be palindrome
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        half = 0
        while x > half: 
            half  = (half * 10) + x % 10 #adds the last digit of x to half
            x = x // 10 #remove the last digit of x
        
        return x == half or x == half//10 # returns true if the half equals the rest of x 

    # the or condition is to check when the number has odd digit that we shouldnt consider the last part of the half
        

        
        