class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        sum = 0
        counter= 0
        left, right = 0, len(people)-1
        while left < right:
            if people[left] + people[right] <= limit:
                left+= 1
                right -= 1
            else:    
                right -=1
            counter += 1
        if left == right:
            counter += 1
        
        return counter



