# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.list= []
        

    def addNum(self, num: int) -> None:
        idx=bisect_left(self.list,num)
        self.list.insert(idx,num)
        

    def findMedian(self) -> float:
        n= len(self.list)
        if n%2==0:
            ans=  self.list[n//2] + self.list[n//2-1]
            return ans/2
        else:
            return self.list[n//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()