# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode()
        ans= dummy
        while list1 or list2:
            if list1:
                val1= list1.val
            else: val1= float(inf)
            if list2: val2= list2.val
            else: val2= float(inf)
            if  val1 < val2 :
                dummy.next= ListNode(list1.val)
                list1= list1.next
                
            else:
                dummy.next= ListNode(list2.val)
                list2= list2.next
            dummy= dummy.next
        return ans.next