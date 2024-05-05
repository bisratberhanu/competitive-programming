# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        strans=''
        
        while num!=0:

            if 1 & num:
                strans+='0'
            else:
                strans+= '1'
            num= num >> 1
        strans= strans[::-1]
        
        return int(strans,2)