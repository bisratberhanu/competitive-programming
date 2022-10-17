class MinStack:

    def __init__(self):
        self.s1=[]
        

    def push(self, val: int) -> None:
        self.s1.append(val)
        

    def pop(self) -> None:
        self.s1.pop()
        

    def top(self) -> int:
        return self.s1[-1]
        

    def getMin(self) -> int:
        x= min(self.s1)
        return x
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()