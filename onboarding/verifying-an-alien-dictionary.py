class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        for i in range(len(words)-1):
            if not self.helper(words[i], words[i+1], order):
                return False
        return True        
        
    def helper(self, str1, str2, order):
        if str1 == "" and str2 == "":
            return True
        elif str1 != "" and str2 == "":
            return False
        elif str1 == "" and str2 != "":
            return True
        elif order.find(str1[0]) > order.find(str2[0]):
            return False  
        elif order.find(str1[0]) < order.find(str2[0]):
            return True
        elif order.find(str1[0]) == order.find(str2[0]):
            return self.helper(str1[1:], str2[1:], order)

            
        