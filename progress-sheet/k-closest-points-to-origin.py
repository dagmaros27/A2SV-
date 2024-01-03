class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = defaultdict(int)

        for i in range(len(points)):
            d = points[i][0]**2 + points[i][1]**2
            dic[i] = d
        
        sorted_dic = sorted(dic.items(), key=lambda x:x[1])
        ans = []
        wanted = 0
        print(sorted_dic)
        for i in sorted_dic:
            ans.append(points[i[0]])
            wanted += 1
            if wanted == k:
                break

        return ans
