class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        oper= ["+","-","*","/"]
        ans=0
        for val in tokens:
        
            if val in oper:
                oper1,oper2= stack.pop(), stack.pop()
                ans= int(eval(oper2+val+oper1))
                stack.append(str(ans))
            else:
                stack.append(val) 
        return int(stack[-1])
