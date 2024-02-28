class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))
        r,d = 0,0

        while len(set(queue)) > 1 :
            vote = queue.popleft()
            if vote == 'R':
                if d:
                    d -=1
                    continue
                r += 1
            else:
                if r:
                    r -= 1
                    continue
                d += 1
            queue.append(vote)
        
        return "Radiant" if queue[0] == "R" else "Dire"
            