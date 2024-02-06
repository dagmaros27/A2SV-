from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tt = Counter(t)
        ss = defaultdict(int)
        setter = set()
        l = 0
        required_chars = len(t)
        min_length = float('inf')
        min_window = ""

        for r in range(len(s)):
            if s[r] in tt:
                if ss[s[r]] < tt[s[r]]:
                    required_chars -= 1
                ss[s[r]] += 1

                while required_chars == 0:
                    if s[l] in tt:
                        if ss[s[l]] <= tt[s[l]]:
                            if r - l + 1 < min_length:
                                min_length = r - l + 1
                                min_window = s[l:r + 1]
                            required_chars += 1
                        ss[s[l]] -= 1
                    l += 1

        return min_window
