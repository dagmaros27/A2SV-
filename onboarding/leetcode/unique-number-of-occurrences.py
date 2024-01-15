class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        setter = set()

        for  i in counter.values():
            if i in setter:
                return False
            setter.add(i)

        return True