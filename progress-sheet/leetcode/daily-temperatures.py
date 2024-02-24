class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []
        ans = [0]* (n)
        counter = 0
        for i in range(n):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                idx = stk.pop()
                ans[idx] = i - idx
            stk.append((i))
        return ans


        