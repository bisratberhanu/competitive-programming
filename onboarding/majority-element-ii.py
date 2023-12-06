class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq_dic= Counter(nums)
        ans=[]
        for key in freq_dic:
            if freq_dic[key] > n/3:
                ans.append(key)
        return ans 
