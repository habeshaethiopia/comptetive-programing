# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path=[]
        def rec(r, v):
            if r:
                if r.left:
                    rec(r.left,v+str(r.val))
                if r.right:
                    rec(r.right,v+str(r.val))
                if not r.left and not r.right:
                    path.append(v+str(r.val))
        x=0
        rec(root,'')
        for i in path:
            x+=int(i)
        return x