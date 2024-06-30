# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            if not root:
                return ''
            l,r='',''
            l=dfs(root.left)
            if not root.left and root.right:
                l= '()'
            r= dfs(root.right) 
            return (
                "("
                +str(root.val)
                + l
                + r
                + ")"
            )
        return dfs(root)[1:-1]