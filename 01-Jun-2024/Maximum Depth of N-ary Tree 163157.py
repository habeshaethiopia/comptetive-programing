# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        q=deque()
        if root:
            q.append(root)
        ans=0
        while q:
            for i in range(len(q)):
                x=q.popleft()
                if x:
                    q.extend(x.children)
            ans+=1
        return ans