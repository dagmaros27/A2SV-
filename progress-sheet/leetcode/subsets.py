class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr,idx):
            if len(curr) > 0:
                ans.append(curr.copy())
            
            for i in range(idx+1, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i)
                curr.pop()
        
        ans = [[]]
        backtrack([], -1)
        return ans

        
            
        