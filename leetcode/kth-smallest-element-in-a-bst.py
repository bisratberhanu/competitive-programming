# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr=[] # to store the the sorted values of the tree
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return arr[k-1]