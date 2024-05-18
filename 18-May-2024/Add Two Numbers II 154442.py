# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        a1 = []
        while l1:
            a1.append(l1.val)
            l1 = l1.next
        a2 = []
        while l2:
            a2.append(l2.val)
            l2 = l2.next
        n = max(len(a1), len(a2))
        a1 = [0] * (n - len(a1)) + a1
        a2 = [0] * (n - len(a2)) + a2
        ans=[]
        carry=0
        for i in range(n-1,-1,-1):
            temp=a1[i]+a2[i]+carry
            ans.append(temp%10)
            carry=temp//10
        if carry!=0:
            ans.append(carry)
        n=len(ans)
        root= ListNode(ans[-1])
        temp=root
        for i in range(n-2,-1,-1):
            # print(root)
            new= ListNode(ans[i])
            temp.next=new
            temp=temp.next
        return root
