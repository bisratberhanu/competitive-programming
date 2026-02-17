#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        for i in range(32):
            reversed_n = reversed_n << 1 | (n & 1)
            n >>= 1
        
        return reversed_n


            

# @lc code=end
