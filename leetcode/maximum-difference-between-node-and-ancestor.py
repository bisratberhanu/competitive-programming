# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def recur(node,minval,maxval):
            if not node:
                return maxval-minval
            
            maxval= max(maxval, node.val)
            minval= min(minval, node.val)
            
            left= recur( node.left, minval,maxval)
            
            right= recur(node.right, minval, maxval)

            return(max(left,right))
        
        return recur(root, root.val, root.val)