class Node:
    def __init__(self,val,next=None):
        self.val= val
        self.next=next

class MyLinkedList:

    def __init__(self):
        self.head= Node(1,None)
        self.length=0
    def get(self, index: int) -> int:
        if self.length<= index:
            return -1 
        length=-1
        current =  self.head
        while length!=index:
            current= current.next
            length+=1
        return current.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length,val)

    def deleteAtIndex(self, index: int) -> None:
        if self.length<= index:
            return None 
        length=0
        current =  self.head
        while length!=index:
            current= current.next
            length+=1
        
        current.next= current.next.next
        self.length-=1

        

    def addAtIndex(self, index: int,val) -> None:
        if self.length< index:
            return None 
        length=0
        current =  self.head
        while length!=index:
            current= current.next
            length+=1

        inserted_node= Node(val, current.next)
        current.next= inserted_node
        print(self.head)
        self.length+=1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)