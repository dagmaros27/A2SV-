class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pf = [0] * (len(nums)+1)

        if len(nums) == 1:
            return nums[0] if nums[0] == k else 0
        for i in range(1,len(pf)):
            pf[i] = pf[i-1] + nums[i-1]
        counter = 0
        #brute force
        # for i in range(len(pf)):
        #     for j in range(len(pf)):
        #         if pf[i] - pf[j] == k:
        #             counter += 1

        pfmap = defaultdict(int)
        counter = 0
        for i in range(len(pf)):
            diff = pf[i] - k
            if diff in pfmap: #instead of using while loop add the frequency to the counter
                counter += pfmap[diff]
            pfmap[pf[i]] += 1
        return counter

