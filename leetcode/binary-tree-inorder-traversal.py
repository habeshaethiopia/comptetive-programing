# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            ans=[]
            if root.left:
                ans.extend(self.inorderTraversal(root.left))
            ans+=[root.val]
            if root.right:
                ans.extend(self.inorderTraversal(root.right))
            print(ans)
            return ans