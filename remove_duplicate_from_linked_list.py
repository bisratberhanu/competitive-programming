# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        ans=ListNode()
        dummy=ans 
        while head:
            if head.val not in list1:
                list1.append(head.val)
                ans.next= ListNode(head.val)
                ans= ans.next
            head= head.next
        return dummy.next
        
