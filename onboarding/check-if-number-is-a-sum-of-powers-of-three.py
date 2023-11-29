
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>1:
            val,rem= divmod(n,3)
            if rem==2:
                return False 
            n= val
        return True
        
