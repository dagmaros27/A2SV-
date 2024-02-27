class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(curr,idx):
            print(idx,curr)

            if sum(curr) == target:
                if curr not in ans:
                    ans.append(curr.copy())
            
            for i in range(idx,len(candidates)):
                if sum(curr) + candidates[idx] > target:
                    continue
                curr.append(candidates[i])
                backtrack(curr,i)
                curr.pop()

        ans = []
        backtrack([],0)
        return ans