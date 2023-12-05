class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candie_num= max(candies)
        ans=[]
        for candy_num in candies:
            ans.append(candy_num+extraCandies>=max_candie_num)
        return ans 