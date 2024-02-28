# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        New=TreeNode(val)
        if not root:
            return New
        temp=root
        while temp and(temp.right or temp.left):
            if val <= temp.val:
                if temp.left:
                    temp=temp.left
                else:
                    break
            elif val >temp.val:
                if temp.right:
                    temp=temp.right
                else:
                    break
     
        if val <= temp.val:
            temp.left=New
        else:
            temp.right=New
        return root