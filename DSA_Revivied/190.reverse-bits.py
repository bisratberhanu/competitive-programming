#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    
    def reverseBits(self, n: int) -> int:
        def int_to_bits(n):
            if n <= 1:
                return str(n)
            bits = ""
            while n != 0:
                val, mod = divmod(n,2)
                n = val
                bits += str(mod)
            return bits
        reversed_bits = int_to_bits(n)
        reversed_bits += "0" * (32 - len(reversed_bits))
        reversed_num = 0
        for i in range(31,-1,-1):
            reversed_num +=  int(reversed_bits[i])*pow(2,31-i)
        return reversed_num


            

# @lc code=end

