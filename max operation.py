 def maxOperations(self, nums: List[int], k: int) -> int:
        l=0 
        r= len(nums)-1
        counter=0
        nums.sort()
        while l<r:
            sum=nums[l]+ nums[r]
            if sum<k:
                l+=1
            elif sum>k:
                r-=1
            elif sum==k:
                r-=1
                l+=1
                counter+=1
        return counter