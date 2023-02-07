def isPowerOfFour(self, n: int) -> bool:
        x=1
        if n==1:
            return True
        while x<n:
            x*=4
            if x==n:
                return True
        return False