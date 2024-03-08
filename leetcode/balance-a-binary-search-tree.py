# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def rec(r):
            return rec(r.left)+[r.val]+ rec(r.right) if r else []
        path=rec(root)
        def divconc(path):
            if path:
                mid=len(path)//2
                root=TreeNode(path[mid])
                root.left=divconc(path[:mid])
                root.right=divconc(path[mid+1:])
                return root
            return None
        return divconc(path)