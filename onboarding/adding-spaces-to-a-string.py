class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
            sentence = ""
            ind = 0
            for i in spaces:
                sentence += s[ind:i]
                sentence += " "
                ind = i
            
            sentence += s[ind:]

            return sentence
            

