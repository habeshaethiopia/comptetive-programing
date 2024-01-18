class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l=0
        c=0
        w={}
        ans=float('inf')
        for i in range(len(cards)):
            if not cards[i] in w:
                w[cards[i]]=i
            else:
                ans=min(i-w[cards[i]]+1, ans)
                w[cards[i]]=i
        return -1 if ans==float('inf') else ans

