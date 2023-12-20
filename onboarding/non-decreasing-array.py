class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        counter=0
        for i in range(1,len(nums)):
            if nums[i]< nums[i-1]:
                counter+=1
                if counter>1:
                    return False
                if i-1==0:
                    nums[i-1]== nums[i]
                else:
                    if nums[i-2]<=nums[i]:
                        nums[i-1]=nums[i]
                    else:
                        nums[i]= nums[i-1]
        return True

         