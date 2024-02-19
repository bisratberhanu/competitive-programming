class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        ans=0
        for i,brac in enumerate(s):
            if brac== "(":
                stack.append(0)
            else:
                mul= stack.pop()
                if mul==0:
                    val=1
                else:
                    val= mul*2
                if not stack:
                    ans+=val
                else:
                    stack[-1]+= val
        return ans 

        
        