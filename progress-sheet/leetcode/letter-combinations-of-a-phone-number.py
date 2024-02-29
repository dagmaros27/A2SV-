class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r","s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y","z"]
        }

        def backtrack(numIdx, letterIdx, word):
            if len(word) == len(digits):
                ans.append("".join(word.copy()))
                return
            
            for i in range(numIdx,len(digits)):
                num = digits[i]
                
                for j in range(len(hmap[num])):
                    
                    letter = hmap[num][j]
                    word.append(letter)

                    backtrack(i+1, j+1,word)
                    word.pop()


        if len(digits)== 0:
             return []   
        ans = []    
        backtrack(0,0,[])

        return ans

        