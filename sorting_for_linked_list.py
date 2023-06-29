# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def insertionSortList(self, head):
        arr=[]
        while head:
            arr.append(head.val)
            head= head.next
        arr.sort()
        ans= ListNode()
        curr=ans
        for i in arr:
            curr.next= ListNode(i)
            curr= curr.next
        return ans.next