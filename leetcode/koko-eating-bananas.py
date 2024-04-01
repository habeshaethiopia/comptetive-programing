class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=sum(piles)
        mn=r
        while l<=r:
            mid=(l+r)//2
            eath=0
            
            for i in piles:
                eath+=ceil(i/mid)
            # print(mid, eath, l ,r)
            if eath <=h:
                mn=min(mn,mid)
                r=mid-1
            else:
                l=mid+1
        return mn


            