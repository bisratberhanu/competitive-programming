class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
       #changing each even number to zero and odd number to one and calculating the prefix sum
        acc=0
        for i in range(len(nums)):
            if nums[i]%2==0:
               nums[i]= acc
            else:
                acc+=1
                nums[i]=acc
        counter_dict= defaultdict(int) #a dictionary to hold the the frequency of prefixsums
        counter_dict[0]=1
        ans= 0
        for i in range(len(nums)):
            ans+= counter_dict[nums[i]-k]
            counter_dict[nums[i]]+=1
        return ans 
        
