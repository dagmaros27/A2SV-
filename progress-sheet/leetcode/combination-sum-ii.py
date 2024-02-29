class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(curr, idx):
            if sum(curr) == target:
                ss = sorted(curr) 
                if ss not in ans:
                    ans.append(ss)
                return
            if sum(curr) > target or  idx >= len(candidates):
                return

            # Pick
            curr.append(candidates[idx])
            backtrack(curr, idx + 1)
            curr.pop()

            while idx < len(candidates) - 1 and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backtrack(curr, idx + 1)
            
        ans = []
        backtrack([], 0)
        return ans
