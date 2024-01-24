# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next
            fast=fast.next
            slow=slow.next
        mid=slow
        pri=None
        cur=slow
        while cur:
            next=cur.next
            cur.next=pri
            pri=cur
            cur=next
        haf=head
        while haf!= mid:
            if pri.val!= haf.val:
                return False
            print(pri.val, haf.val)
            pri=pri.next
            haf=haf.next
        return True