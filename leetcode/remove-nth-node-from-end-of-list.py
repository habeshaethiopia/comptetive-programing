# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        c=0
        while temp:
            c+=1
            temp=temp.next
        temp=head
        for i in range(c-n-1):
            temp=temp.next
        print(temp.val)
        if n==c:
            return head.next
        temp.next=temp.next.next if temp.next else None
        return head 