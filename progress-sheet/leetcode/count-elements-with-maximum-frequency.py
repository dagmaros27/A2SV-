class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)

        maxCounter = max(counter.values())

        return sum(counter[i] for i in counter if counter[i] == maxCounter)
        # ans = 0
        # for i in counter:
        #     if counter[i] == maxCounter:
        #         ans += counter[i]
        
        # return ans
                