class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # the prefix sum and suffix sum approach
        prefix=[0]* len(nums)
        suffix=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                if nums[i]==1:
                    prefix[i]=0
                else:
                    prefix[i]=1
            elif nums[i]==0:
                prefix[i]= prefix[i-1]+1
            else:
                prefix[i]= prefix[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                if nums[i]==1:
                    suffix[i]=1
                else:
                    suffix[i]=0
            elif nums[i]==1:
                suffix[i]= suffix[i+1]+1
            else:
                suffix[i]=suffix[i+1]
        
        ans=[]
        maxval= -1
        for i in range(len(nums)+1):
            if i==0:
                temp1=0
                temp2= suffix[i]
            elif i== len(nums):
                temp1= prefix[i-1]
                temp2= 0
            else:
                temp1= prefix[i-1]
                temp2= suffix[i]
            count= temp1+temp2
            if count> maxval:
                ans=[i]
                maxval=count
            elif count==maxval:
                ans.append(i)
        return ans
        