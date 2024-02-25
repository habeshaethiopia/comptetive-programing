# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans=[]
        n=0
        t=head 
        while t:
            ans.append(t)
            t=t.next
        n=len(ans)//k
        r=len(ans)%k
        x=0
        final=[]
        y=0
        for i in range(k):
            if r:
                y=1
                r-=1
            else:
                y=0
            if x<len(ans):
                if x:
                    ans[x-1].next=None
                final.append(ans[x])
            else:
                final.append(None)
            x+=n+y
        
        return final