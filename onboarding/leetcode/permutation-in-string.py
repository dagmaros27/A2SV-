class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        size = len(s1)
        hmap = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            hmap[s2[r]] += 1

            if r-l+1 == size:
                if hmap == count1:
                    return True
                hmap[s2[l]] -= 1
                if hmap[s2[l]] == 0:
                    del hmap[s2[l]]
                l += 1
        
        return False
