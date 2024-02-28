# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans= 0
        def sumFinder(node):
            if node == None:
                return 
            
            if low<= node.val <= high:
                self.ans+= node.val
            sumFinder(node.left)
            sumFinder(node.right)

            return self.ans
        
        sumFinder(root)
        return self.ans