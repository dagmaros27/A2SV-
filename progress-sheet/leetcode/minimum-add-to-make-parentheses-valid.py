class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openNedded = 0
        closeNedded = 0

        for i in range(len(s)-1,-1,-1):
            if s[i] == ")":
                openNedded += 1
            if s[i] == "(":
                if openNedded == 0:
                    closeNedded += 1
                else:
                    openNedded -= 1
        
        return openNedded + closeNedded

        