class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(curr,setter):
            # print(curr,setter)
            if len(curr) == len(nums):
                ans.append(curr.copy())
                # print(ans,curr)
                # setter.clear()
                return
            

            for i in range(len(nums)):
                if nums[i] not in setter:
                    curr.append(nums[i])
                    setter.add(nums[i])
                    backtrack(curr,setter)
                    curr.pop()
                    setter.remove(nums[i])

        ans = []
        curr = []
        setter = set()
        backtrack(curr,setter)
        return ans

        