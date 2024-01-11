from collections import Counter, defaultdict

class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        n = len(s)
        l = 0
        hmap1 = {i: counter[i] - (n // 4) for i in counter if counter[i] > n // 4}
        hmap2 = defaultdict(int)
        min_length = float('inf')

        for r in range(n):
            if r < n and s[r] in hmap1:
                hmap2[s[r]] += 1

            while l < n and all(hmap2[char] >= hmap1[char] for char in hmap1): ##this all function???
                min_length = min(min_length, r - l + 1)
                if l < n and s[l] in hmap2:
                    hmap2[s[l]] -= 1
                l += 1

        return 0 if min_length == float('inf') or min_length < 0 else min_length
