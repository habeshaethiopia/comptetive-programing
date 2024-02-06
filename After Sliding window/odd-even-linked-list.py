# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        te=head
        to=head.next if te else None
        he=None
        ho=None
        tempe=None
        tempo=None
        while to and te and to.next:
            newo=ListNode(to.val)
            newe=ListNode(te.val)
            to=to.next.next
            te=te.next.next
            if not he:
                he=newe
                tempe=newe
            else:
                tempe.next=newe
                tempe=tempe.next
            print(newe.val)
            if not ho:
                ho=newo
                tempo=newo
            else:
                tempo.next=newo
                tempo=tempo.next
        if te:
            newe=ListNode(te.val)
            if not he:
                he=newe
                tempe=newe
            else:
                tempe.next=newe
                tempe=tempe.next
        if to:
            newo=ListNode(to.val)
            if not ho:
                ho=newo
                tempo=newo
            else:
                tempo.next=newo
                tempo=tempo.next
        if tempe:
            tempe.next=ho
        return he
            
