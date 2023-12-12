class Solution:
    def isHappy(self, n: int) -> bool:
        seen= set()
        while True:
            ans=0
            while n>0:
                val,mod= divmod(n,10)
                ans+=(mod)**2
                n=val
            print(ans)
            if ans in seen:
                return False
            if ans==1:
                return True
            seen.add(ans)
            n=ans

