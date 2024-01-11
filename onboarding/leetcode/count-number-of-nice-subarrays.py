class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        counter = 0
        
        odd_counter = 0
        l = 0
        subarr = 0
        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                odd_counter += 1
                counter = 0
            while odd_counter == k:
                counter += 1
                if nums[l] % 2 != 0:
                    odd_counter -= 1
                l += 1
            subarr += counter
        return subarr

