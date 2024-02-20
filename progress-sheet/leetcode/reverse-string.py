class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(i,j):
            if i >= j :
                return
            else:
                s[i], s[j] = s[j], s[i]
                return swap(i+1,j-1)
        return swap(0, len(s)-1)
        



