class Node:
    def __init__(self,val,next=None,back=None):
        self.val= val
        self.next= next
        self.back=back 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.node= Node(homepage)

    def visit(self, url: str) -> None:
        added= Node(url)
        self.node.next= added
        added.back= self.node
        self.node= added
    def back(self, steps: int) -> str:
        while steps>0 and self.node.back:
            self.node= self.node.back
            steps-=1
        return self.node.val
        

    def forward(self, steps: int) -> str:
        while steps>0 and self.node.next:
            self.node= self.node.next
            steps-=1
        return self.node.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)