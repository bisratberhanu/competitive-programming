class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def recur(n):
            if n==1:
                return True
            elif n<1:
                return False  
            return recur(n/4)
        return recur(n)