class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        l=0
        r=citations[-1]
        mx=0
        while l<=r:
            mid=(l+r)//2

            temp=bisect_left(citations, mid)
            if n-temp>=mid:
                mx=max(mx,mid)
                l=mid+1
            else:
                r=mid-1
        return mx

