# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            prev= None
            while head:
                new_node= ListNode(head.val)
                new_node.next= prev
                prev= new_node
                head= head.next
            return new_node
        
        new_node= (reverse(head))
        while head:
            if head.val!= new_node.val:
                return False
            head= head.next
            new_node= new_node.next
        return True 



        