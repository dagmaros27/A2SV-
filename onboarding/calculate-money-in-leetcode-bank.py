class Solution:
    def totalMoney(self, n: int) -> int:
        week = 0

        money = 0
        i = 1
        while i <= n:
            money += (i % 7 + week)

            if i % 7 == 0:
                money += 7
                week += 1
            i += 1
        
        return money
        
        