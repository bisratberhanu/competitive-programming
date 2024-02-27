class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets=[]

        def backTrack(idx, each_subset):
            # base case 
            if len(each_subset) <= len(nums):
                subsets.append(each_subset[:])
                

            for i in range(idx, len(nums)):
                each_subset.append(nums[i])
                backTrack(i+1, each_subset)
                each_subset.pop()
        
        backTrack(0, [])
        return subsets

        
