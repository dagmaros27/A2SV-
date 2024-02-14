class Solution:
    def numRabbits(self, answers: List[int]) -> int:
    #     answers.sort()
    #     ans = answers[0] + 1

    #     for i in range(1,len(answers)):
    #         if answers[i] == 0:
    #             ans += 1 
    #         elif answers[i] != answers[i-1]:
    #             ans += answers[i] + 1

        count = defaultdict(int)
        answers.sort()
        ans = 0
        for answer in answers:
            if answer == 0:
                ans += 1
            else:
                if answer not in count or count[answer] ==0:
                    ans += answer + 1
                    count[answer] = answer
                else:
                    count[answer] -= 1


        return ans
        