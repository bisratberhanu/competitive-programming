class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        def custom(x):
            if x==val:
                return 1000
            else : return x
        nums.sort(key= custom)
        if val in nums:
            return nums.index(val)
        return len(nums)
        

        












































































        


        