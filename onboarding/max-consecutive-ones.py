class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter=0
        list1=[]
        for i in nums:
            if i==1:
                counter+=1
            else:
                list1.append(counter)
                counter=0
            list1.append(counter)
        return max(list1)
