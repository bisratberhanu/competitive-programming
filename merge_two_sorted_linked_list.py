# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2 ) :
        dummy= ListNode()
        ans=dummy
        while list1 and list2:
                val1= list1.val
                val2=list2.val
                if val1<val2:
                    fake =  ListNode(val1)
                    dummy.next = fake
                    list1=list1.next
                
                else:
                    fake=ListNode(val2)
                    dummy.next=fake
                    list2=list2.next
                dummy = dummy.next
                
        dummy.next = list2
        if list1:
            dummy.next = list1
            
        return ans.next