class Solution:
    def smallestNumber(self, num: int) -> int:
        arr = list(map(int, list(str(abs(num)))))
        if num > 0:
            arr.sort()
            first = float('inf')
            for i in range(len(arr)):
                if arr[i] < first and arr[i] != 0:
                    first = arr[i]
            arr.remove(first)
            arr.insert(0, first) 
        else:
            arr.sort(reverse=True)         
        num = int("".join(map(str, arr))) if num > 0 else -int("".join(map(str, arr)))
        
        return num
            