class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def dayCounter(capacity):
            hold = 0
            counter = 0
            for w in range(len(weights)):
                if hold + weights[w] > capacity:
                    counter += 1
                    hold = 0
                hold += weights[w]
            counter += 1