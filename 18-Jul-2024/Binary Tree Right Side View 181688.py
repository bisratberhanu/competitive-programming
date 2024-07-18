# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(node, depth):
            if not node:
                return
            # If this is the first node we're visiting at this depth, add it to the answer
            if depth == len(ans):
                ans.append(node.val)
            # First visit the right subtree, then the left subtree
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return ans