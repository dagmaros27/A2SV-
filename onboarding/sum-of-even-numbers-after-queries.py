class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        even_total = sum([i for i in nums if i%2 == 0 ])
        ans = []

        for query in queries:
            if nums[query[1]] % 2 == 0:
                even_total -= nums[query[1]]
            
            nums[query[1]] += query[0]
            if nums[query[1]] % 2 == 0:
                even_total += nums[query[1]]
            ans.append(even_total)
            
        return ans
                