class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_count = 0
        count = 0
        l = 0
        for r in range(len(s)):
            if s[r] in vowels:
                count += 1
            if r-l == k:    # i dont know why not r-l+1
                if s[l] in vowels:
                    count -= 1
                l += 1
            max_count = max(count, max_count)
            
        return max_count
