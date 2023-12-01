class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) -1
        reversed = ''
        while i >= 0:
            if s[i] == "#":
                asci = int(s[i-2:i])
                # print(asci)
                letter = chr(96 + asci)
                reversed += letter
                i -= 2
            else:
                asci = int(s[i])
                # print(asci)
                letter =  chr(96 + asci)
                reversed += letter
            i -= 1
        
        return reversed[::-1]
