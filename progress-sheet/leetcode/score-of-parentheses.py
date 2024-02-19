class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else:
                a = stack.pop()
                if a == '(':
                    stack.append(1)
                else:
                    if stack and stack[-1] == "(":
                        stack.pop()    
                    stack.append(a*2)
            if len(stack) > 1 and stack[-1] != '(' and stack[-2] != "(":
                a = stack.pop() + stack.pop()
                stack.append(a) 


        return stack.pop()
            
