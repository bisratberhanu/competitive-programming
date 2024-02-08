class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefixsum= [0 for i in range(len(s))]
        
        for shift in shifts:
            if shift[2]==0:
                prefixsum[shift[0]]-=1
                if shift[1]!= len(s)-1:
                    prefixsum[shift[1]+1]+=1
            else:
                prefixsum[shift[0]]+=1
                if shift[1]!= len(s)-1:
                    prefixsum[shift[1]+1]-=1
        acc=0
        print(prefixsum)
        for i in range(len(prefixsum)):
            acc+= prefixsum[i]
            prefixsum[i]= acc
        print(prefixsum)
        ans=""
        for i in range (len(prefixsum)):
            ans+= chr((ord(s[i])-ord('a')+prefixsum[i])%26+ ord('a'))
        return ans 


