class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counter=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if j!=i and nums[j]==nums[i] and (i*j)%k==0:
                    counter+=1
        return counter
        