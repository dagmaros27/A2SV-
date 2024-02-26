class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # def valid(arr,k):
        #     if len(arr) != k:
        #         return False
        #     for i in range(1,len(arr)):
        #         if arr[i] <= arr[i-1]:
        #             return False
        #     return True
        
        def backtrack(candidate):
            if len(candidate) == k:
                ans.append(candidate.copy())
                return
            last = candidate[-1] if candidate else 0

            for i in range(last+1,n+1):
                candidate.append(i)
                backtrack(candidate)
                candidate.pop()
        ans = []
        backtrack([])

        return ans
            




        