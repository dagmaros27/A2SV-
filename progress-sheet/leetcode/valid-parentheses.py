class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        strArr = list(s)
        if(len(strArr)%2 != 0):
            return False
        for s in strArr:
            if(s == '(' or s=='{' or s=='['):
                stack.append(s)          
            elif(s==')' ):
                if(stack and stack[-1] == '('):
                    stack.pop()
                else:
                    return False                
            elif(s=='}'):
                if(stack and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False 
            elif(s==']'):
                if(stack and stack[-1] == '['):
                    stack.pop()
                else:
                    return False 
        if(stack):
            return False
        return True