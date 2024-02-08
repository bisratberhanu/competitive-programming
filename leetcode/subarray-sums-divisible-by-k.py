class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic= defaultdict(int)
        summ=0
        dic[0]= 1
        ans=0
        for i in range(len(nums)):
            summ+= nums[i]
            ans+= dic[summ%k]
            dic[summ%k]+=1
        return ans 
        