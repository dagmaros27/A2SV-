class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums) // 3
        counter = Counter(nums)
        ans = []
        for i in counter.keys():
            if counter[i] > freq:
                ans.append(i)
        
        return ans


        