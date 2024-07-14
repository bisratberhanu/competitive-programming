# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        list1=[]
        list2=[]
        for i in s:
            if i!="#":
                list1.append(i)
            else: 
                if list1: list1.pop()
        for i in t:
             if i!="#":
                list2.append(i)
             else:
                if list2: list2.pop()
        return list1==list2

