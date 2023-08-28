# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis1=[]
        while head:
            lis1.append(head.val)
            head= head.next
        lis1.sort()
        ans= ListNode()
        dummy= ans
        for i in lis1:
            dummy.next= ListNode(i)
            dummy= dummy.next
        return ans.next
        
