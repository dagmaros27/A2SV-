class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # total1 = 0

        # for i in p:
        #     total1 += ord(i)
        
        # total2 = 0
        # for i in range(0,len(p)):
        #     total2 += ord(s[i])

        # l = 0
        # ans = []
        # for i in range(len(p), len(s)):
        #     if total1 == total2:
        #         ans.append(l)
        #     total2 -= ord(s[l])
        #     total2 += ord(s[i])
        #     l += 1
        # if total1 == total2:
        #     ans.append(l)
        

        dic1 = Counter(p)

        dic2 = Counter(s[:len(p)])

        l = 0
        ans = []
        for i in range(len(p), len(s)):
            if dic1 == dic2:
                ans.append(l)
            dic2[s[l]] -= 1
            if dic2[s[l]] == 0:
                del dic2[s[l]]
            dic2[s[i]] = dic2.get(s[i], 0) + 1
            l +=1
        if dic1 == dic2:
            ans.append(l)
        return ans