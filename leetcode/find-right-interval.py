class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic= {}
        for i in range(len(intervals )):
            dic[intervals[i][0]]= i
        start= [ val[0] for val in intervals]
        start.sort()
        ans=[]
        for val in intervals:
            idx= bisect_left(start, val[1])
            if idx== len(start):
                ans.append(-1)
            else:
                temp= dic[start[idx]]
                ans.append(temp)
        return ans  