# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesshead, morehead= ListNode(), ListNode()
        dummyless, dummymore= lesshead, morehead 
        
        while head:
            
            if head.val < x:
                lesshead.next= ListNode(head.val)
               
                lesshead= lesshead.next
                
            else:
                
                morehead.next= ListNode(head.val)
                
                morehead= morehead.next
                
            head= head.next
        
        if lesshead:
            lesshead.next= dummymore.next
        return dummyless.next
