class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def dayCounter(capacity):
            hold = 0
            counter = 0
            for w in range(len(weights)):
                if hold + weights[w] > capacity:
                    counter += 1
                    hold = 0
                hold += weights[w]
            counter += 1
            return True if counter <= days else False
        
        l, h = max(weights), sum(weights)+1

        while l <= h:
            mid = (l+h)//2
            if dayCounter(mid):
                h = mid -1
            else:
                l = mid+1
        return l
        
        