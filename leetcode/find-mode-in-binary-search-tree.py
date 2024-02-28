# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def res(root):
            return [root.val]+res(root.left)+res(root.right)if root else []
        val=Counter(res(root))
        mx=max(val.values())
        
        print(mx)
        ans=[i for i in val if val[i]==mx]
        return ans