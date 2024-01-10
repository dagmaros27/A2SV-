class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_Ans = 0
        l = 0
        hmap = defaultdict(int)
        for r in range(len(answerKey)):
            hmap[answerKey[r]] += 1
            while hmap['T'] > k:
                hmap[answerKey[l]] -= 1
                l += 1      
            max_Ans = max(max_Ans, r-l+1)

        #need to do for both because i dont know the distribution
        l = 0
        hmap.clear()
        for r in range(len(answerKey)):
            hmap[answerKey[r]] += 1
            while hmap['F'] > k:
                hmap[answerKey[l]] -= 1
                l += 1      
            max_Ans = max(max_Ans, r-l+1)
        
        return max_Ans
