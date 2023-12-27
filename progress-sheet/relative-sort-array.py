class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        def comp(item):
            if item in arr2:
                return arr2.index(item)
            return 1000
        arr1.sort(key = comp)
        idx = 0
        for i in arr1:
            
            if i not in arr2:
                break
            idx += 1

        print(idx)
        return arr1[:idx] + sorted(arr1[idx:])

      