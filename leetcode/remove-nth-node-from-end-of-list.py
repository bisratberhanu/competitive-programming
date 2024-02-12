# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        left,right= head, head
        previous= head
        for i in range(n):
            right= right.next
        if right==None:
            return head.next
        while right and right.next:
            
            right= right.next
            left= left.next
        
        left.next= left.next.next
        return head
