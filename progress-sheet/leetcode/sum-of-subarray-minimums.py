class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        arr.append(0) #we append 0 at the end to pop out any element left at the end
        n = len(arr)
        res = 0
        for i in range(n):
            mnm = 1 #counts the number of elements it has poped or less than on the stack
            #when arr[i] is smaller than all nums in the stack it means with all the subbary of arr[i] and nums in the stack arr[i] is the minimum
            #so we add the minimum count of the others to the arr[i]'s count
            while stack and stack[-1][0] > arr[i]:
                num, count = stack.pop()
                res += (num * count * mnm)
                mnm += count
            stack.append((arr[i], mnm ))
        
        return res % (10**9+7)
    
