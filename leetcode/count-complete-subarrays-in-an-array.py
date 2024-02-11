class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        numcompleted= len(Counter(nums))
        dic=defaultdict(int)
        ans=left=0
        
        for right in range(len(nums)):
            dic[nums[right]]+=1
            while len(dic)==numcompleted:
                dic[nums[left]]-=1
                if dic[nums[left]]==0: del dic[nums[left]]
                ans+=len(nums)-right
                left+=1
        return ans 
