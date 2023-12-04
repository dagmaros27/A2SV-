class Solution:
    def printVertically(self, s: str) -> List[str]:
        # indexes = defaultdict(list)
        # words = s.split()
        # ans = []

        # for word in words:
        #     j = 0
        #     while j < len(word):
        #         indexes[j].append(word[j])
        #         j += 1
        
        # for  i in indexes.values():
        #     ans.append("".join(i))

        # return ans

        words = s.split()
        maxlen = max([len(i) for i in words])
        word_matrix = [[" "] * maxlen for i in range(len(words))]

        for  i in range(len(words)):
            j = 0
            while j < len(words[i]):
                word_matrix[i][j] = words[i][j]
                j += 1

            
        verts = defaultdict(str)

        for word in word_matrix:
            i = 0
            while i < len(word):
                verts[i] += word[i]
                i += 1
               
                
        result = [val.rstrip() for val in verts.values()]

        return result

