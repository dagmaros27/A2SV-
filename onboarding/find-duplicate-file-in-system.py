class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        filtered_hashmap = defaultdict(list)
        #brute force
        for i in paths:
            arr = i.split(" ")
            for i in range(1,len(arr)):
                file = arr[i].split(".txt")
                key = file[1]
                value = arr[0] + "/" + file[0] + ".txt"
                hashmap[key].append(value)

        for k, v in hashmap.items():
            if len(v) >= 2:
                filtered_hashmap[k] = v
        result = list(filtered_hashmap.values())

        return result
