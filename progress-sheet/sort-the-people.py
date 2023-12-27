class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        

        # for i in range(len(heights)):
        #     for j in range(len(heights)-1):
        #         if heights[j] < heights[j+1]:
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
        #             names[j], names[j+1] = names[j+1], names[j]
        
        # return names

        maxNum = max(heights)

        count = [0]* (maxNum + 1)

        for i in range(len(heights)):
            count[heights[i]] = names[i]
        names.clear()
        count.reverse()
        for i in count:
            if isinstance(i, str):
                names.append(i)
        return names