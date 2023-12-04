class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic= Counter(nums)
        ans=0
        for val in dic:
            n= dic[val]
            ans+= n*(n-1)//2
        return ans 

         