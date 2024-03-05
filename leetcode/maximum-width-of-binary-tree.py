# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic= defaultdict(list)
        def rec(root, num, row):
            if root:
                dic[row].append(num)
                rec(root.left,2*num+1, row+1)
                rec(root.right,2*num+2, row+1)
        rec(root,0,0)
        print(dic)
        ans=0
        for i in dic:
            ans=max(ans, max(dic[i])-min(dic[i])+1)
        return ans

