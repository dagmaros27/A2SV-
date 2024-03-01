class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < (k*(k+1))//2:
            return []
        def backtrack(candidate):
            if len(candidate) == k and sum(candidate) == n:
                ans.append(candidate.copy())
                return
            last = candidate[-1] if candidate else 0

            for i in range(last+1,10):
                if sum(candidate) + i > n:
                    continue
                candidate.append(i)
                backtrack(candidate)
                candidate.pop()
        ans = []
        backtrack([])

        return ans
        