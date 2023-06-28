# Definition for singly-linked list.
#
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        arr=[]
        while head:
            arr.append(head.val)
            head= head.next
        part_arr= arr[left-1:right]
        part_arr.reverse()
        arr[left-1:right]= part_arr
        
        ans= ListNode()
        cur=ans
        for i in arr:
            cur.next= ListNode(i)
            cur= cur.next
        return ans.next



