# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divconc(start, end):
            mid = floor((start + end) / 2)

            node=TreeNode(nums[mid])
           
            if start > end:
                return None
            node.left = divconc(start, mid-1)
            node.right = divconc(mid + 1, end)
            return node

        return divconc(0, len(nums)-1)
