# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
   
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp_dict={0:1}
        for total in range(1,target+1):
            dp_dict[total]=0
            for val in nums:
                dp_dict[total]+= dp_dict.get(total-val,0)
        return dp_dict[target]

        
       
        
        

        