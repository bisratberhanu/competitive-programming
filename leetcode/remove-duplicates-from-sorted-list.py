# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev= None
        ans= head
        while head and head.next:
            cur = head.next
            while cur and  cur.val == head.val:
                cur= cur.next
            head.next= cur
            head= head.next
                
             
        return ans 