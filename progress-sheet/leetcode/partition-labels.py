class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        setter = set()
        curr = 0
        last= -1
        ans = []
        for i in range(len(s)):
            if s[i] not in setter:
                curr += counter[s[i]]
                setter.add(s[i])
            curr -=1

            if curr == 0:
                ans.append(i - last)
                last = i
        
        return ans

  


        