class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board), len(board[0])
        path = set() #to track we dont revisit the same letter

        def backtrack(x,y,idx):
            if idx == len(word): # if we pass to the last index i.e we get the word
                return True
            
            if (x < 0 or y < 0 or x >= rows or y >= cols    #if coord is out of bound or if already visited or 
                or (x,y) in path or board[x][y] != word[idx]): #coord letter is not same as the current letter in word
                return False
            

            path.add((x,y))

            res = (backtrack(x+1,y,idx+1) or backtrack(x-1,y,idx+1) or # we try moving in all four direction from the four position
                    backtrack(x,y+1,idx+1) or backtrack(x,y-1,idx+1))
            
            path.remove((x,y))

            return res

        for i in range(rows): #bruteforce our way from each possible start position
            for j in range(cols):
                if backtrack(i,j,0): 
                    return True
        return False
        