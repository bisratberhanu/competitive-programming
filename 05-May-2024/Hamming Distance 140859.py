# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/



class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def bit_count(num):
            return bin(num).count('1')
        xor= x^y
        return bit_count(xor)