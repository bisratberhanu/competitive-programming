# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        unsorted = []
        for idx, num in enumerate(nums):
            strNum= str(num)
            strAns=''
            for digit in strNum:
                strAns+= str(mapping[int(digit)])
            unsorted.append((int(strAns), idx,  num))
        unsorted.sort()
        print(unsorted)
        return [ tup[2] for tup in unsorted]
