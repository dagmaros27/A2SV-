class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = ["" for i in range(len(s))]

        for i in range(len(indices)):
            arr[indices[i]] = s[i]
            # arr[i] = s[indices[i]] , this one doesnt work but i dont know why
        return "".join(arr)

