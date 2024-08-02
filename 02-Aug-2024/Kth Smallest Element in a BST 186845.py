# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def rec(rt):
            return rec(rt.left) + [rt.val] + rec(rt.right) if rt else []

        return rec(root)[k - 1]
