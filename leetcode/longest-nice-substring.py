class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def checker(string):
            for letter in string:
                if letter.lower()==letter:
                    if letter.upper() not in string:
                        return False
                else:
                    if letter.lower() not in string:
                        return False
            return True
        ans=''
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                temp=s[i:j+1]
                if checker(temp) and len(temp)>len(ans):
                    ans=temp
        return ans 

           
