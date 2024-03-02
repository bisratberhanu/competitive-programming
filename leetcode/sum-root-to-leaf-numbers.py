# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def recur(node, string):
            if not node.left and not node.right:
                print(string)
                self.ans+= int(string+ str(node.val))
                return
            if node.left:
                recur(node.left, string+str(node.val))
            if node.right:
                recur(node.right, string+ str(node.val))
        
        recur(root, "")
        return self.ans


            