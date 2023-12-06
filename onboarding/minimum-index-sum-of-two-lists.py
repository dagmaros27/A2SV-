class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least_index = float("inf")
        commons = {}
        ans = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j] and sum([i,j]) <= least_index:
                    least_index = sum([i,j])
                    commons[list1[i]] = least_index

        for key,value in commons.items():
            if value == least_index:
                ans.append(key)

        return ans
