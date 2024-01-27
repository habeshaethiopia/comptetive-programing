class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l=0
        w=set()
        ans=float('inf')
        for i in range(len(cards)):
            while cards[i] in w:
                ans=min(i-l+1, ans)
                # print(cards[l:i+1])
                w.discard(cards[l])
                l+=1
            w.add(cards[i])
        return -1 if ans==float('inf') else ans

