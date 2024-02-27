# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symmetric(node1, node2):
            if not node1 and not node2:
                return True 
            if not node1 and node2:
                return False 
            if not node2 and node1:
                return False 

            if node1.val != node2.val:
                return False 
            
            val1= symmetric(node1.left, node2.right)
            val2= symmetric(node1.right, node2.left)

            return val1 and val2
        return symmetric(root, root)