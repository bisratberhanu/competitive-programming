def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h1 = h2 = head
        while h2 and (h2:= h2.next):
            if h2: h2 = h2.next;h1= h1.next
        return h1