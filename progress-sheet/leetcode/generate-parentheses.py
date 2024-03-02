class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # def validate(curr):
        #     if len(curr) < 2*n:
        #         return False
            
        #     stack = []
            
        #     for s in curr:
        #         if s == '(':
        #             stack.append(s)          
        #         elif s==')' :
        #             if stack and stack[-1] == '(':
        #                 stack.pop()
        #             else:
        #                 return False                
            
        #     if(stack):
        #         return False
        #     return True


        def backtrack(curr, opens,closes):
            # if opens == 0 and closes == 0 and len(curr) == 2*n:
            #         ans.append("".join(curr))
            #         return
            # if opens:
            #     curr.append('(')
            #     backtrack(curr,opens-1,closes)

            #     curr.pop()
            #     backtrack(curr,opens-1,closes)

            # if closes and closes > opens:
            #     curr.append(')')
            #     backtrack(curr,opens,closes-1)

            #     curr.pop()
            #     backtrack(curr,opens,closes-1)

            if opens == closes == n:
                ans.append("".join(curr))
                return
            if opens < n:
                curr.append("(")
                backtrack(curr,opens+1,closes)
                curr.pop()
            if closes < opens:
                curr.append(")")
                backtrack(curr,opens,closes+1)
                curr.pop()


        ans = []
        backtrack([],0,0)
        return ans



