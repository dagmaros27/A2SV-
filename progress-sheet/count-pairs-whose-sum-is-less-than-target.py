class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        #bruteforce
        # n = len(nums)
        # counter = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] < target:
        #             counter += 1
                
        # return counter

        # dic = {i:nums[i] for i in range(len(nums))}

        # sorted_dic = dict(sorted(dic.items(), key = lambda x : x[1]))
        counter =0
        nums.sort()
        left,right = 0, len(nums)-1

        while left < right:
            sum = nums[left]+ nums[right]
            if sum < target:
                counter += (right - left)
                left += 1
            else:
                right -= 1

        return counter
            
        







                

