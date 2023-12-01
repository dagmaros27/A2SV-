class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I": 1,
            "V" : 5,
            "X" : 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M" :1000,
        }
        

        i = 0
        num = 0 
        while i < len(s):
            num += romans[s[i]]
            if i+1 < len(s):
                if s[i] == 'I':
                    if s[i+1] == "V" or s[i+1] == "X":
                        num -= (romans[s[i]] *2)
                elif s[i] == "X":
                    if s[i+1] == "L" or s[i+1] == "C":
                        num -= (romans[s[i]] *2)
                elif s[i] == "C":
                    if s[i+1] == "D" or s[i+1] == "M":
                        num -= (romans[s[i]] *2)
            i += 1
        return num
            
            
                
