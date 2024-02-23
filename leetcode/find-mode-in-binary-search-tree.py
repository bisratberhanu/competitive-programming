# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr=[]
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def mode(root):
            if not root:
                return
            self.arr.append(root.val)
            mode(root.left)
            mode(root.right)
        mode(root)
        dic= Counter(self.arr)
        maxfreq= float(-inf)
        
        for val in dic:
            maxfreq= max(maxfreq, dic[val])
        ans=[]
        for val in dic:
            if dic[val]== maxfreq:
                ans.append(val)
        return ans 



        
        