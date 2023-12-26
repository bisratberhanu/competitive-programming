class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # using selection sort
        for i in range(len(names)-1):
            for j in range(i+1, len(names)):
                if heights[j]>= heights[i]:
                    names[j],names[i]= names[i], names[j]
                    heights[j],heights[i]= heights[i], heights[j]
        return names 