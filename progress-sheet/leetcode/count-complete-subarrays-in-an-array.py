class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(set(nums))
        counter = defaultdict(int)
        subarrs = 0
        l = 0
        for r in range(len(nums)):
            counter[nums[r]] += 1
            if set(counter.keys()) == set(nums):
                subarrs += 1 + (len(nums)-r-1)
            while len(counter.keys())>= n:
                counter[nums[l]] -= 1
                if counter[nums[l]] == 0:
                    del counter[nums[l]]
                if set(counter.keys()) == set(nums):
                    subarrs += 1 + (len(nums)-r-1)
                l += 1
        return subarrs

            




        
        