class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans=[]
        ptr1,ptr2=0,0
        while ptr1<len(firstList) and ptr2<len(secondList):
            mincommon= max(firstList[ptr1][0], secondList[ptr2][0])
            maxcommon=  min(firstList[ptr1][1], secondList[ptr2][1])
            if maxcommon>=mincommon:
                ans.append([mincommon,maxcommon])
            if firstList[ptr1][1]< secondList[ptr2][1]:
                ptr1+=1
            else:
                ptr2+=1
        return ans 


        