class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        while head:
            val= head.val
            l.append(val)
            head=head.next
        #print(l)
        l.reverse()
        #print(l)
        ans=ListNode()
        dummy=ans
        for i in l:
            #ans.val=i
            
            fake=ListNode(i)
            ans.next=fake
            ans=ans.next
            #print(ans)
        
        return dummy.next