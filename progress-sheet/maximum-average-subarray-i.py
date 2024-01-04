class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        l = 0
        for r in range(k,len(nums)):
            curr_sum -= nums[l]
            curr_sum += nums[r]
            max_sum = max(max_sum, curr_sum)
            l += 1
        avg = max_sum / k

        return avg
        