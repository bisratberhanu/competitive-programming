class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:  
        
        acc,ans=0,0
        dic= defaultdict(int)
        dic[0]=1
        for i in range(len(nums)):
            acc+= nums[i]
            ans+=  dic[acc-goal]
            dic[acc]+=1
        return ans 