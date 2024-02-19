class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(len(palindrome)//2): # if we cant find a way till the half since the other half is the same we cant find 
            if palindrome[i]!="a":
                return palindrome[:i]+"a"+palindrome[i+1:]
        return palindrome[:-1]+"b" if len(palindrome)>1 else ""