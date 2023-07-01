# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def oddEvenList(self, head):
        evencurr,oddcurr= ListNode(), ListNode()
        evenlist,oddlist= evencurr,oddcurr
        counter=1
        while head:
            if counter%2==0:
                evencurr.next= ListNode(head.val)
                evencurr= evencurr.next
            else:
                oddcurr.next=ListNode(head.val)
                oddcurr= oddcurr.next
            head= head.next
            counter+=1
        oddcurr.next= evenlist.next
        return oddlist.next