class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums)==0:
            return '0'
        lisnums= list(map(str,nums))
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if lisnums[j]+lisnums[i]> lisnums[i]+lisnums[j]:
                    lisnums[j],lisnums[i]= lisnums[i],lisnums[j]
        return ''.join(lisnums)
        
        

        