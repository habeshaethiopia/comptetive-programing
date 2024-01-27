# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        pri=None
        while temp:
            pri=temp
            temp=temp.next    
            if temp and pri.val==temp.val:
                while temp and pri.val==temp.val:
                    temp=temp.next
                pri.next=temp
        return head
                
        