class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=[]
        minval= inf 
        for i in range(len(list1)):
            if list1[i] in list2:
                j= list2.index(list1[i])
                tot= i+j
                if tot < minval:
                    ans= [list1[i]]
                    minval= tot
                elif tot== minval:
                    ans.append(list1[i])
        return ans 
            
