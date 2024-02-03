class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dic=defaultdict(int)
        dic[0]+=1
        ans=0
        prefixsum=0
        for i in range(len(nums)):
            prefixsum+= nums[i]
            if prefixsum-k in dic:
                ans+= dic[prefixsum-k]
               
                
            dic[prefixsum]+=1
        return ans  
            
