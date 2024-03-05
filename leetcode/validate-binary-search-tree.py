# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, mn, mx):
            if root:
                if not (mn < root.val < mx):
                    return False
                return validate(root.left, mn, root.val) and validate(
                    root.right, root.val, mx
                )
            return True

        return validate(root, -float("inf"), float("inf"))
