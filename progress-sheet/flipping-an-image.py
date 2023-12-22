class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        

        for row in image:

            i,j = 0, len(row)-1
            while i <= j:
                if i == j:
                   row[i] = 0 if row[i] == 1 else 1
                   break            
                row[i], row[j] = row[j], row[i]
                row[i] = 0 if row[i] == 1 else 1
                row[j] = 0 if row[j] == 1 else 1
                j -= 1
                i += 1


        return image
    



