# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        new=None
        sm=0
        ans=None
        while dummy:
            if dummy.val==0 and sm !=0:
                if new:
                    new.next=ListNode(sm)
                    
                    new=new.next
                else:
                    new=ListNode(sm)
                    ans=new
                sm=0
            else:
                sm+=dummy.val
            dummy=dummy.next
        return ans
            