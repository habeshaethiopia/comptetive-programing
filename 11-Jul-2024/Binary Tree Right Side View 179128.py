# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=[]
        if root:
            q.append(root)
        ans=[]
        while q:
            last=None
            temp=[]
            for p in q:
                if p.left:
                    temp.append(p.left)
                if p.right:
                    temp.append(p.right)
                last=p
            ans.append(last.val)
            q=temp
        return ans
