class Solution:
    def maxConsecutiveAnswers(self, answerkey: str, k: int) -> int:
        left,right=0,0
        temp,ans=0,0
        while right<len(answerkey):
            if answerkey[right]=='F':
                temp+=1
            while temp>k:
                if answerkey[left]=='F':
                    temp-=1
                left+=1
            ans= max(ans,right-left+1)
            

            right+=1
        left2,right2=0,0
        temp2,ans2=0,0
        while right2<len(answerkey):
            if answerkey[right2]=='T':
                temp2+=1
            while temp2>k :
                if answerkey[left2]=='T':
                    temp2-=1
                left2+=1
            ans2= max(ans2,right2-left2+1)
            right2+=1
        return max(ans,ans2)