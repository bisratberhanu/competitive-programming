class Solution:
    def simplifyPath(self, path: str) -> str:
        arr= path.split("/")
        print(arr)
        stack=[]
        for val in arr:
            if val== ".." and stack:
                stack.pop()
            elif val!= "." and val!= "" and val!= "..":
                stack.append(val)
        ans=""
        print(stack)
        for i in range(len(stack)):
            if stack[i]== "":
                continue 
            if stack:
                ans+= '/'+ stack[i]
        if not ans:
            return "/"
        return ans 

                