# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def rec(rt):
            return rec(rt.left) + [rt.val] + rec(rt.right) if rt else []

        return rec(root)[k - 1]
