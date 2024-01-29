class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # ans = []
        # for i in range(len(arr)-1):
        #    maxNum =  max(arr[i:])
        #    maxIdx = arr.index(maxNum)
        #    ans.append(maxIdx+1)
        #    arr[i:maxIdx+1] =  arr[i:maxIdx+1][::-1] 
        #    arr[i:] = arr[i:][::-1]
        #    arr.append(i)
        # return ans

        ans = []
        for i in range(len(arr)-1, -1, -1):
            if arr[i] != i+1: 
                for j in range(i-1, -1, -1): 
                    if arr[j] == i+1:
                        break
                arr[:j+1] = arr[:j+1][::-1] 
                arr[:i+1] = arr[:i+1][::-1] 
                ans.append(j+1)
                ans.append(i+1)
        return ans
        


