# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            s=head
            f=head
            while f and f.next:
                f=f.next
                s=s.next
                f=f.next if f else None
            print(s.val)
            return s
        else:
            return None