class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_int= ''.join(map(str,digits))
        num= int(str_int)
        num+=1
        str_int_new= str(num)
        ans= list(str_int_new)
        for i in range(len(ans)):
            ans[i]= int(ans[i])
        return ans 