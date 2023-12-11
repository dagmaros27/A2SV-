
class Solution:
   def arrayChange(self,nums: List[int], operations: List[List[int]]) -> List[int]:
    map1 = {}

    for o,n in reversed(operations):
        map1[o] = map1[n] if n in map1 else n
    for i,num in enumerate(nums):
        if num in map1:
            nums[i] = map1[num]
    return nums
