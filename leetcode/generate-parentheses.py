class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def isvalid(arr):
            stack=[]
            for brac in arr:
                if brac=="(":
                    stack.append("(")
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
            return len(stack)==0

        def backTrack(generated,opened, closed):
            if opened< closed or opened>n:
                return 
            if len(generated)== 2*n:
                if isvalid(generated[:]):
                    ans.append("".join(generated))
                return 
            
            generated.append("(")
            backTrack(generated,opened+1, closed)
            generated.pop()
            generated.append(")")
            backTrack(generated, opened, closed+1)
            generated.pop()

        backTrack([],0,0)
        return ans 
        




            

        