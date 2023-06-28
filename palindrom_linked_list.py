# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        lis=[]
        while head:
            val= head.val
            
            lis.append(val)
            head= head.next
        l2= lis.copy()
        l2.reverse()
        if lis==l2:
            return True
        return False 