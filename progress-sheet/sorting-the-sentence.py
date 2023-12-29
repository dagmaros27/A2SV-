class Solution:
    def sortSentence(self, s: str) -> str:
        dic = defaultdict(str)

        for i in s.split():
            dic[int(i[-1])] = i[:-1]
        
        ans = [""] * len(dic)
        for key,val in dic.items():
            ans[key-1] = val
        
        return " ".join(ans)


