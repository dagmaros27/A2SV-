class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = set()

        for i in matches:
            winners.add(i[0])
            losers.add(i[1])
        winnersList = list(winners - losers)
        winnersList.sort()

        losers.clear()
        removables = set()
        for  i in matches:
            if i[1]  in losers:
                removables.add(i[1])
            else:
                losers.add(i[1])
        
        losersList = list(losers - removables)
        losersList.sort()

        return [winnersList,losersList]
