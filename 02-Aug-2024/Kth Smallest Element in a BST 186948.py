# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lis=[] # to store the the sorted values of the tree
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            lis.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return lis[k-1]