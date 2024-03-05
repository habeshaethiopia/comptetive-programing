# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)

        def rec(root, row):
            if root:
                dic[row].append(root.val)
                rec(root.left, row + 1)
                rec(root.right, row + 1)
        rec(root, 0)
        ans=[]
        for i in dic:
            if i%2==0:
                ans.append(dic[i])
            else:
                ans.append(dic[i][::-1])
        return ans