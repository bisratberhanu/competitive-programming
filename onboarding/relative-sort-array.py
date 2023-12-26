class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic= Counter(arr1)
        ans=[]
        for val in arr2:
            ans.extend([val]*dic[val])
        temp=[]
        for val in arr1:
            if val not in arr2:
                temp.append(val)
        temp.sort()
        ans.extend(temp)
        return ans 