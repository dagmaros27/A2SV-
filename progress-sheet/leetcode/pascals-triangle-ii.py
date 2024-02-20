class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            arr = self.getRow(rowIndex-1)
            ans = [1]
            for i in range(len(arr)-1):
                ans.append(arr[i] + arr[i+1])
            ans.append(1)
            return ans
        