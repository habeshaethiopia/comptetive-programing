# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def dfs(h):
            r=[]
            while h:
                r.append(h.val)
                h=h.next
            return r
        arr=dfs(head)
        # print(arr)
        l=0
        r=len(arr)-1
        ans=0
        while l<r:
            ans =max(ans, arr[l]+arr[r])
            r-=1
            l+=1
        return ans
