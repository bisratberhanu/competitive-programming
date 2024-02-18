class Solution:
    def isValid(self, s: str) -> bool:
        validbrackets= ["[]","{}", "()"]
        stack=[]
        for bracket in s:
            if not stack:
                stack.append(bracket)
            else:
                if stack[-1]+ bracket in validbrackets:
                    stack.pop()
                else:
                    stack.append(bracket)
        print(stack)
        return len(stack)== 0