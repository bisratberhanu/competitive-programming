# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        arr_p, arr_q= [],[]

        def valueFinder(node,target,arr):
            if node.val== target.val:
                arr.append(node)
                return
            arr.append(node)
            if node.val > target.val:
                return valueFinder(node.left,target,arr)
            return valueFinder(node.right, target, arr)
        
        valueFinder(root, p, arr_p)
        valueFinder(root,q, arr_q)
        ans=[]
        for i in range(min(len(arr_p), len(arr_q))):
            if arr_p[i].val== arr_q[i].val:
                ans.append(arr_p[i])
        return ans[-1]