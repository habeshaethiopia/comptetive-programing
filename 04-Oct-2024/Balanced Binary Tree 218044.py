# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def rec(root,h):
            if root:
                return max(rec(root.left,h+1),rec(root.right,h+1))
            return h-1
        def check(r,h):
            if r:
                x=r.right
                y=r.left
                if  abs(rec(x,h+1)-rec(y,h+1))<=1:
                    if check(x,h) & check(y,h):
                        return True
                    else:
                        return False
                else:
                    return False
            return True
        
        return check(root,0)


        