# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recl(root):
            return [root.val]+recl(root.left)+recl(root.right) if root else [None]
        def recr(root):
            return [root.val]+recr(root.right)+recr(root.left) if root else [None]
        left=recl(root.left)
        right=recr(root.right)
        print(left,right)
        return recl(root.left)==recr(root.right) if root else True