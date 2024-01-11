class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)

        size = len(cardPoints) - k
        curr = sum(cardPoints[0:size])
        max_sum = total - curr
        l = 0
        for r in range(size,len(cardPoints)):
            curr -= cardPoints[l]
            curr += cardPoints[r]
            l += 1
            curr_sum = total - curr
            max_sum = max(max_sum, curr_sum)
            print(curr_sum)
        
        return max_sum


        