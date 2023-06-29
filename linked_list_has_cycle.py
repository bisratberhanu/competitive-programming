# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head ) -> bool:
        fastptr,slowptr= head,head
        counter=10000
        while fastptr and fastptr.next:
            fastptr= fastptr.next.next
            slowptr= slowptr.next
            if fastptr==slowptr:
                return True
        return False
