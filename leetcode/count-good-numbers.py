class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD= 10**9 + 7
        if n%2==0:
            anseven= pow(5,n//2,MOD)
            ansodd= pow(4, n//2,  MOD)
        else:
            anseven= pow(5,n//2 +1, MOD)
            ansodd= pow(4,n//2, MOD)
        ans= anseven* ansodd

        return ans%(10**9 +7) 
        