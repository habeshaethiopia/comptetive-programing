# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left, right):
            # print(left.val,right.val)
            l = left
            r = right
            pri = None
            head=ListNode()
            temp=head
            while l and r:
                if l.val < r.val:
                    temp.next=ListNode(l.val)
                    temp=temp.next
                    l = l.next
                else:
                    temp.next=ListNode(r.val)
                    temp=temp.next
                    r = r.next
            while r:
                temp.next=ListNode(r.val)
                temp=temp.next
                r = r.next
            while l:
                temp.next=ListNode(l.val)
                temp=temp.next
                l = l.next
                
            return head.next

        def mergesort(left, right):
            
            fast=left
            slow=left
            if left==right:
                return left
            while fast:
                if fast==right:
                    break
                fast=fast.next
                if fast==right:
                    break
                fast=fast.next if fast else fast
                slow=slow.next
            
            t=slow.next
            slow.next=None
            myleft=mergesort(left, slow)
            myright=mergesort(t, right)
            return merge(myleft, myright)

        return mergesort(head, None)
