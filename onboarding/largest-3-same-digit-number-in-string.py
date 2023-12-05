class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=''
        for left in range(len(num)-2):
                if num[left:left+3]== num[left]*3:
                    if len(ans)==0 or int(ans)< int(num[left:left+3]):
                        ans=  num[left:left+3]
        return ans 
