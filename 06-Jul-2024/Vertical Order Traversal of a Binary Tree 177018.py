# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vert = defaultdict(list)

        def rec(r, row, col):
            if r:
                vert[(row, col)].append((r.val))
                rec(r.left, row + 1, col - 1)
                rec(r.right, row + 1, col + 1)

        rec(root, 0, 0)
        # vert dic have the nodes with their row and col
        # we extract vert to temp using their col (same col)
        temp = defaultdict(list)
        # vert.sort(key=lambda x:x[0])
        for i in sorted(vert.keys(), key=lambda x: x[0]):
            temp[i[1]] += sorted(vert[i])

        # print(temp)
        # append to our answer according to their order
        ans = [temp[i] for i in sorted(temp.keys())]
        return ans
