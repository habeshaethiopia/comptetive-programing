# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans=0

        def rec(root, mn, mx):
            nonlocal ans
            if root:
                mn = min(mn, root.val)
                mx = max(mx, root.val)
                ans = max(ans, abs(mx - mn))
                print(root.val, mn, mx)
                rec(root.left, mn, mx)
                rec(root.right,mn ,mx)
        rec(root, float('inf'), -float('inf'))
        return ans
