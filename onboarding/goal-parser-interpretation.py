class Solution:
    def interpret(self, command: str) -> str:
        ans=''
        for i in range(len(command)):
            if command[i]=='G':
                ans+='G'
            elif command[i]==')':
                if command[i-1]=='(':
                    ans+='o'
                elif command[i-1]=='l':
                    ans+='al'
        return ans 