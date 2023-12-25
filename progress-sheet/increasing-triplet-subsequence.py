class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        # find an increasing non-contigous subsequence in the array if you did return true else false
        #brute force
        #the for i, for j, for k method which is O(n)

        f = float("inf")
        s = float("inf")

        for n in nums:
            if n <= f:
                f = n
            elif n <= s:
                s = n
            elif n > s:
                return True
        return False


        

        
        
            
