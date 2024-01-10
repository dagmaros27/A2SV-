class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        setter = set()
        max_score = 0
        curr_score = 0
        l = 0

        for r in range(len(nums)):
            curr_score += nums[r]
            while nums[r] in setter:
                curr_score -= nums[l]
                setter.discard(nums[l])
                l += 1
            max_score = max(max_score, curr_score)
            setter.add(nums[r])

        return max_score