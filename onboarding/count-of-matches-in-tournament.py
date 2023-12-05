class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n >1:
            if n %2 != 0:
                matches += 1
            n = n //2
            matches += n

        return matches
        