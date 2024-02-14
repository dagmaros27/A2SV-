class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        while k > 0:
            if numOnes >0 :
                ans += 1
                numOnes -= 1
            elif numZeros > 0:
                numZeros -= 1
            else:
                numNegOnes -= 1
                ans -= 1
            k -= 1
        return ans

        