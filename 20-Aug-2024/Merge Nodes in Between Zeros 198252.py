# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros




class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We initialize a dummy node to help us easily return the head of the new list
        dummy = ListNode()
        current = dummy
        
        summ = 0
        node = head.next  # Skip the first zero
        
        while node:
            if node.val != 0:
                summ += node.val
            else:
                if summ > 0:
                    current.next = ListNode(summ)
                    current = current.next
                    summ = 0  
            node = node.next
        
        return dummy.next
