class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newlist=[]
        for i in nums:
            counter=0
            for j in nums:
                if i>j:
                    counter+=1
            newlist.append(counter)
        return newlist