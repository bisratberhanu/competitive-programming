# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_time = (n - 1) * 2  
        effective_time = time % cycle_time  
        
        if effective_time < n:
            return effective_time + 1  
        else:
            return n - (effective_time - n + 1)  