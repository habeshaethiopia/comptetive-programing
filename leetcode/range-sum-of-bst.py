# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def rec(root):
            return rec(root.left) + [root.val]+ rec(root.right) if root else []
        ans=0
        for i in rec(root):
            if i>high:
                break
            if i>=low:
                ans+=i
                # print(i)
        return ans