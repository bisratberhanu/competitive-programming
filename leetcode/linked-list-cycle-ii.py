# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowptr,fastptr= head,head
        while fastptr and fastptr.next:
            slowptr=slowptr.next
            fastptr=fastptr.next.next
            if fastptr==slowptr:
                while True:
                    if head==fastptr:
                        return head
                    head= head.next
                    fastptr= fastptr.next

        
