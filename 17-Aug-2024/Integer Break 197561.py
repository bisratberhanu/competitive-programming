# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        dic= {1:1}
        def dp(num):
            if num in dic:
                return dic[num]
            dic[num]=0 if num==n else num
            for i in range(1, num):
                val = dp(i) * dp(num-i)
                dic[num]= max(dic[num], val)
            return dic[num]

        return dp(n)
        



