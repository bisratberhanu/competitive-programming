class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False
        lis=[]
        while x>0:
            val,mod= divmod(x,10)
            lis.append(mod)
            x=val
        print(lis)
        return lis== lis[::-1]


            
         

        