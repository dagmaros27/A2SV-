class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        

        if len(arr) < 3:
            return False

        maxNum = max(arr)

        i = arr.index(maxNum)
        
        if len(arr[:i]) == 0 or len(arr[i+1:]) == 0:
            return False
        sorted_left = sorted(arr[:i+1])
        sorted_right = sorted(arr[i:], reverse = True)

        unique_left = len(set(arr[:i]))
        unique_right = len(set(arr[i:]))

        if sorted_left != arr[:i+1] or sorted_right != arr[i:]:
            return False
        if unique_left != len(arr[:i]) or unique_right != len(arr[i:]):
            return False
        
        return True