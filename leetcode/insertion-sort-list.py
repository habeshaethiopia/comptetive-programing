# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr = head

        while curr and curr.next:
            if curr.val > curr.next.val:
                pre = dummy
                while pre.next.val < curr.next.val:
                    pre = pre.next
                temp = curr.next
                curr.next = temp.next
                temp.next = pre.next
                pre.next = temp
            else:
                curr = curr.next

        return dummy.next