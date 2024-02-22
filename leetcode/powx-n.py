class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastpower(x,n):
            if n==0:
                return 1
            if n<0:
                return 1/ (fastpower(x, abs(n))) 
            if n%2==0:
                return fastpower(x*x,n//2)
            return x* fastpower(x*x, n//2)
        
        return fastpower(x,n )