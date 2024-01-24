# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h1=None
        h2=None
        temp1=None
        temp2=None
        tra=head
        
        while tra:
            new=ListNode(tra.val)
            if x > tra.val:
                if not h1:
                    h1=new
                    temp1=h1
                else:
                    temp1.next=new
                    temp1=temp1.next
            else:
                if not h2:
                    h2=new
                    temp2=h2
                else:
                    temp2.next=new
                    temp2=temp2.next
            
            tra=tra.next
        if temp1:
            temp1.next=h2
        
        return h1 if h1 else h2
        