class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        curr_sum = 0
        max_num  = 0
        counter = 0

        for i in flips:
            curr_sum += i
            max_num = max(max_num, i)
            total = (max_num*(max_num +1))//2
            if total == curr_sum:
                counter += 1
        
        return counter
