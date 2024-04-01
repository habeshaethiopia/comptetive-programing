# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(arr):
            if not arr:
                return None
            mx=max(arr)
            root=TreeNode(mx)
            index=arr.index(mx)
            root.left=build(arr[:index])
            root.right=build(arr[index+1:])
            return root
        return build(nums)