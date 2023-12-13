class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic={}
        # build the dic
        for i in range(len(nums)):
            dic[nums[i]]=i
        for operation in operations:
            idx= dic[operation[0]]
            nums[idx]= operation[1]
            del dic[operation[0]]
            dic[operation[1]]=idx
        return nums

        