class Solution:
    def minimizedStringLength(self, s: str) -> int:
        chars = defaultdict(list)

        for i in range(len(s)):
            chars[s[i]].append(i)

        indexes = []
        for key,value in chars.items():
            if len(value) > 1:
                indexes.append(value[1])
            else:
                 indexes.append(value[0])
        indexes.sort()
        answer = ""
        for i in indexes:
            answer += s[i]

        return len(answer)
