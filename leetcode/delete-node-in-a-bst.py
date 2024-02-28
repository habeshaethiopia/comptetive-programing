# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minval(temp):
            while temp.left:
                temp=temp.left
            return temp
        def delete(temp,key):
            if temp:
                if key < temp.val:
                    temp.left=delete(temp.left,key)
                elif key > temp.val:
                    temp.right=delete(temp.right,key)
                else:
                    if not temp.left:
                        return temp.right
                    elif not temp.right:
                        return temp.left 
                    succer=minval(temp.right)
                    temp.val=succer.val
                    temp.right=delete(temp.right,succer.val)
                        
            else:
                return temp
            return temp
        return delete(root,key)
