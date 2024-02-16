class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # greedy 
        ans= 0
        totsum=0
         
        for i in range(len(nums)):
            if totsum>= n:
                return ans
            while totsum+1< nums[i]:
                patched= totsum+1
                ans+=1
                totsum+= patched
                if totsum>= n:
                    return ans
            totsum+= nums[i]
            

        while totsum<n:
            ans+= 1
            totsum+= totsum+1
        return ans  


