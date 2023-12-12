class Solution:
    def isHappy(self, n: int) -> bool:
        tracked = set()
        return self.happy_recursion(n,tracked)

    def happy_recursion(self,num, tracker):
        sum = 0
        while num > 0:
            digit = num % 10
            sum += digit**2
            num //= 10
        if sum == 1:
            return True
        elif sum in tracker:
            return False
        else:
            tracker.add(sum)
            return self.happy_recursion(sum,tracker)
        



