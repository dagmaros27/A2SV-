class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        firstOdd = 1
        ans = 0
        for i in counter:
            if counter[i]%2 == 0:
                ans += counter[i]
            else:
                if firstOdd:
                    ans += counter[i]
                    firstOdd -= 1
                else:
                    ans += counter[i]-1
                    

             

        return ans
        