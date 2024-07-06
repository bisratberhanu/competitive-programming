# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        stranss=''
        
        while num!=0:

            if 1 & num:
                stranss+='0'
            else:
                stranss+= '1'
            num= num >> 1
        stranss= stranss[::-1]
        
        return int(stranss,2)