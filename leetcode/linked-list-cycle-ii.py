# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=slow=head
        while fast:
            slow =slow.next
            fast=fast.next.next if fast.next else None
            if fast==slow:
                break
        temp=None
        if slow==fast:
            temp=slow
            slow=head
        while temp:
            if temp==slow:
                return slow
            temp=temp.next
            slow=slow.next

        