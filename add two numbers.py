def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ans = dummy
        reminder = 0
        while l1 or l2 or reminder:
            val1, val2 = 0, 0
            if l1:
                val1 = l1.val
                l1 = l1.next

            if l2:
                val2 = l2.val
                l2 = l2.next

            l = ListNode((val1 + val2 + reminder)%10)
            reminder = (val1 + val2 + reminder)//10

            dummy.next = l
            dummy = dummy.next