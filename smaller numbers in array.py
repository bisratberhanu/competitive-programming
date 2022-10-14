class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list=[]
        for values in nums:
            c=0
            for j in nums:
                if values>j:
                    c+=1
            list.append(c)
        return list
    