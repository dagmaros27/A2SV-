class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = []
        i = 0

        while i < len(s):
            arr.append(s[i: i+k])
            i += k
        
        if i < len(s):
            arr.append(s[i:])
        for idx, subs in enumerate(arr):
            if  idx % 2 == 0:
                arr[idx] = subs[::-1]
    
        return "".join(arr)

        