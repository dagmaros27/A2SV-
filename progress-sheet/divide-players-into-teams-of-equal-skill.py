class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        teams = len(skill)//2
        target = sum(skill)//teams

        skill.sort()

        i, j = 0,len(skill)-1
        ans = []
        while i < j:
            if skill[i] + skill[j] == target:
                ans.append([skill[i], skill[j]])
            i += 1
            j -= 1
        if len(ans) != teams:
            return -1
        else :
            total = 0
            for i in ans:
                total += (i[0]*i[1])
            return total
        