class Solution:
    def decodeString(self, s: str) -> str:
        
        stack= []
        for i,val in enumerate(s):
            if val!= "]":
                stack.append(val)
            else:
                temp=""
                while stack[-1] != "[":
                    temp+= stack.pop()
                stack.pop()
                digit=""
                while stack and stack[-1].isdigit():
                    digit+= stack.pop()
                digit= digit[::-1]
                multi= int(digit)
                temp= temp[::-1]
                temp= multi*temp
                for val in temp: stack.append(val)
        
        return "".join(stack)

