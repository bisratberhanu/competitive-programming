# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def pairSum(self, head):
        arr=[]
        while head:
            arr.append(head.val)
            head= head.next
        ptr1= 0
        ptr2= len(arr)-1
        init= -10000000 #initial value to check from
        while ptr1<ptr2:
           init=max(arr[ptr1]+arr[ptr2] ,init)
           ptr1+=1
           ptr2-=1
        return init 