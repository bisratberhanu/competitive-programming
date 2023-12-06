class Solution:
    def totalMoney(self, n: int) -> int:
        ans=[1]
        for i in range(1,n):
            if i%7==0:
                ans.append(ans[i-7]+1)
            else:
                ans.append(ans[i-1]+1)
        return sum(ans)