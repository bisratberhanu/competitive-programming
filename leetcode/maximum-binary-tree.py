# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(l,r):
            if l>r:
                return 
            
            maxval= max(nums[l:r+1])
            idx= nums.index(maxval)
            root= TreeNode(maxval)
            root.left= helper(l, idx-1)
            root.right= helper(idx+1, r)

            return root
        return helper(0, len(nums)-1)
