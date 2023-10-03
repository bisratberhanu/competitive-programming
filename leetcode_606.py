class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def generate_paren_str(node: TreeNode):
            if not node:
                return ""
            
            left_str = generate_paren_str(node.left)
            right_str = generate_paren_str(node.right)
            level_str = f"{node.val}({left_str})({right_str})"
            return level_str
        
        def strip_excessive_parenthesis(parenthesis_str: str):
            final_str = []
            n = len(parenthesis_str)
            i = 0
            while i < n:
                # Both childs empty. Omit
                if i+4 <= n and parenthesis_str[i:i+4] == "()()":
                    i += 4
                    continue
                    
                # Right child breaks one to one mapping. Omit
                if i+3 <= n and (parenthesis_str[i:i+3] == "())" or parenthesis_str[i:i+3] == ")()"):
                    i += 2
                    continue
                    
                final_str.append(parenthesis_str[i])
                i += 1
            return "".join(final_str)
                
        return strip_excessive_parenthesis(generate_paren_str(root))
