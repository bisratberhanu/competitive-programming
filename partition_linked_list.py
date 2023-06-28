# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def partition(self, head, x: int):
        lesslist,greaterlist= ListNode(),ListNode()
        lesscurr, greatercurr= lesslist,greaterlist
        while head:
            if head.val<x:
                lesscurr.next=ListNode(head.val)
                lesscurr= lesscurr.next
                
            else:
                greatercurr.next= ListNode(head.val)
                greatercurr= greatercurr.next
            head= head.next
        
        head1= lesslist.next
        head2= greaterlist.next
        ans=head1
        while head1 and head1.next:
            head1=head1.next
        if head1:
            head1.next = head2
        else:
            return head2
        return ans