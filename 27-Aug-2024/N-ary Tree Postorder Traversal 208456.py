# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

        
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        def traverse(node):
            if not node:
                return
            # Visit all children first
            for child in node.children:
                traverse(child)
            # Then visit the node itself
            result.append(node.val)
        
        traverse(root)
        return result