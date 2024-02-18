# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # to find the length of the linked list and array arr for the answer 
        arr=[]
        cur=head
        n=0
        while cur:
            cur=cur.next
            n+=1
        width,reminder= divmod(n,k)
        cur=head
        for i in range(k):
            head= write=ListNode(None)
            for j in range(width+(i<reminder)):
                write.next= write=ListNode(cur.val)
                if cur:cur=cur.next
            arr.append(head.next)
        return arr 
        
            
            
            


           

        