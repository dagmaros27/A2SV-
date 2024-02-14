class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs.sort(key = lambda x: (x[0] - x[1]))
        ans = 0
        for i in range(len(costs)//2):
            ans += costs[i][0] + costs[len(costs)-1-i][1]

        return ans
#the objective function of the greedy approach is the profit or loss from choosing one city 
#i.e the difference between the two cities