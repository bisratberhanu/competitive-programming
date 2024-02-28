# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr= [[] for i in range(2000)]

        def leveler(level, node):
            if not node:
                return
            arr[level].append(node.val)
            leveler(level+1, node.left)
            leveler(level+1, node.right)
        
        leveler(0, root)
        ans=[]
    
        for lis in arr:
            if lis:
                ans.append(lis)
        i=0
        main_ans=[]
        for val in ans:
            if i%2==0:
                main_ans.append(val)
            else:
                
                val.reverse()
                
                main_ans.append(val)
            i+=1
        return main_ans 

