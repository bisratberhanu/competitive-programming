class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets=[]
        seen= set()
        def backTrack(idx, subset_each):
            subset_each_sorted= sorted(subset_each)
            tupled= tuple(subset_each_sorted)
            
            if len(subset_each)<= len(nums) and tupled  not in seen:
                subsets.append(subset_each_sorted)
                seen.add(tupled)
            
            for i in range(idx, len(nums)):
                subset_each.append(nums[i])
                backTrack(i+1, subset_each)
                subset_each.pop()
        
        backTrack(0,[])

        subsets.sort()
        return subsets
            
