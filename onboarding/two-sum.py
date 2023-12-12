class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = defaultdict(int)

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hmap and i != hmap[diff]:
                return [hmap[diff],i]
            hmap[nums[i]] = i
        
        return
            