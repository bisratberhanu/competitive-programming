class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_pivot=[]
        more_pivot=[]
        equal_pivot=[]
        for num in nums:
            if num<pivot:
                less_pivot.append(num)
            elif num>pivot:
                more_pivot.append(num)
            else:
                equal_pivot.append(num)

        less_pivot.extend(equal_pivot)
        less_pivot.extend(more_pivot)
        return less_pivot