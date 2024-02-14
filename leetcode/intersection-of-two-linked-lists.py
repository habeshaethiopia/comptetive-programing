# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        t1=headA
        nodes=set()
        while t1:
            nodes.add(t1)
            t1=t1.next
        t2=headB
        while t2:
            if t2 in nodes:
                return t2
            t2=t2.next
        return None