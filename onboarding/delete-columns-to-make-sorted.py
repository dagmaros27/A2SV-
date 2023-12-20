class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columns = 0
        letters = [i for i in strs[0]]
        flags = [False] * len(strs[0])
        for str in strs:
            for i in range(len(str)):                   
                if letters[i] > str[i]:
                    flags[i] = True
                else:
                    letters[i] = str[i]
        return flags.count(True)            
            
