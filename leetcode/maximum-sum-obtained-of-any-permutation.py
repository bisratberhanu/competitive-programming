class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix= [0]* len(nums)
        for start,end in requests:
            prefix[start]+=1
            if end!= len(nums)-1:
                prefix[end+1]-=1
        acc=0
        for i in range(len(prefix)):
            acc+= prefix[i]
            prefix[i]= acc
        prefix.sort(reverse= True)
        nums.sort(reverse= True)
        ans=0
        for i in range(len(prefix)):
            ans+= prefix[i]*nums[i]
        return ans%(10**9+7) 