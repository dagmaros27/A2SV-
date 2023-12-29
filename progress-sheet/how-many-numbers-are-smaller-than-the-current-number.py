class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        maxNum = max(nums)
        counter = [-1]* (maxNum+1)
        
        for i in range(len(nums)):
            if counter[nums[i]] == -1:
                counter[nums[i]] = 1
            else:
                counter[nums[i]] += 1
        counted = 0
        for i in range(len(counter)) :
            if counter[i] == -1:
                continue
            temp = counter[i]
            counter[i] = counted
            counted += temp
        
        for i in range(len(nums)):
            nums[i] = counter[nums[i]]
        
        return nums


        # dic = defaultdict(int)
        # arr = nums.copy()
        # arr.sort()
        # for i in range(len(arr)):
        #     if  dic[arr[i]]:  #the problem here is it gets false for  the first result 0
        #        continue           
        #     dic[arr[i]] = i+1
        # res = []

        # for i in range(len(nums)):
        #     res.append(dic[nums[i]]-1)
        # return res

              

            


        



