class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)

        totalRem = total%p
        if totalRem == 0:
            return 0
        #it is actually subarray sum equals to k but k here is the target
        # and we care about the length here so instead of the frequencies 
        # we use {pf elements: index} in the dictionary  
        #we need to take care of numbers other than the totalRem but have the same modulo
        length = len(nums)
        currSum = 0
        counter = defaultdict(int)

        for i in range(len(nums)):
            currSum += nums[i]
            rem = currSum % p
            target = (p+ rem - totalRem) % p

            if target in counter:
                length = min(length, i - counter[target] )
            
            if target == 0 and i != len(nums)-1:
                length = min(length, i+1)
            counter[rem] = i

        
        return length if length < len(nums) else -1


        

