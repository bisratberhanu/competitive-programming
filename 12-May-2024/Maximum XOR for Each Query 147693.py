# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans=[]
        xorval= 0
        for val in nums:
            xorval= xorval ^ val
        

        for i in range(len(nums)):
            ans.append(xorval ^ ((2**maximumBit)-1))
            xorval= xorval ^ nums[-1]
            nums.pop()
        
        return ans 



