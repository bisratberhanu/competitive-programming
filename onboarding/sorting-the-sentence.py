class Solution:
    def sortSentence(self, s: str) -> str:
        arr= s.split()
        dic={}
        for word in arr:
            num= int(word[-1])
            dic[num]= word[0:-1]
        ans=''
        for i in range(1,len(arr)+1):
            ans+=dic[i]
            ans+=' '
        ans= ans.strip()
        return ans 



        