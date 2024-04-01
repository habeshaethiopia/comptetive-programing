# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1=[]
        a2=[]
        while l1:
            a1.append(str(l1.val))
            l1=l1.next
        while l2:
            a2.append(str(l2.val))
            l2=l2.next
        print(a1, ''.join(a1[::-1]))
        result=eval(''.join(a1[::-1]) +'+'+ ''.join(a2[::-1]))
        ans =[ ListNode(int(i)) for i in str(result) ]
        ans=ans[::-1]
        for i in range(len(ans)-1):
            ans[i].next=ans[i+1]
        return ans[0]