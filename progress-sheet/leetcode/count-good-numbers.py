class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odds = pow(4, n//2, 10**9 +7 )
        evens = pow(5, ceil(n/2), 10**9+7)
        return (odds * evens)% (10**9+7)
        