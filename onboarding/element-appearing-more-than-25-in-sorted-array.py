class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        temp = len(arr)/4
        dic= Counter(arr)
        print(dic)
        for val in dic:
            if dic[val]>temp:
                return val
        