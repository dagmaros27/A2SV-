class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pf = [0]*n
        for i in shifts:
            k = 1 if i[2] == 1 else -1 
            pf[i[0]] += k
            if i[1] < n-1:
                pf[i[1]+1] -= k
        for i in range(1,len(pf)):
            pf[i] += pf[i-1]
        
        ans = []

        for i in range(n):
            new_i = chr((ord(s[i]) - ord('a') + pf[i]) % 26 + ord('a'))
            ans.append(new_i)

        return "".join(ans)
