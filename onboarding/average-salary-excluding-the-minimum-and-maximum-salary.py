class Solution:
    def average(self, salary: List[int]) -> float:
        minimum = min(salary)
        maximum = max(salary)
        total= 0
        for i in salary:
            total += i

        return (total-minimum-maximum)/(len(salary)-2)

        