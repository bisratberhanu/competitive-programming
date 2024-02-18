class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        stack=[]
        for i in s:
            if i=='(':
                stack.append('(')
            else:
                if stack:
                    stack.pop()
                else:
                    count+=1
        return count + len(stack)