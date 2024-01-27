# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x1=list1
        x2=list2
        head=None
        temp=head
        while x2 or x1:
            v1=x1.val if x1 else float('inf')
            v2=x2.val if x2 else float('inf')
            if v1>=v2:
                new=ListNode(x2.val)
                x2=x2.next
            else:
                new=ListNode(x1.val)
                x1=x1.next
            print(new.val)
            if not head:
                head=new
                temp=new
            else:
                temp.next=new
                temp=temp.next
        return head


                

