class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pf = [0] * (len(gain)+1)

        for i in range(1, len(gain)+1):
            pf[i] = pf[i-1] + gain[i-1]
        
        return max(pf)
        