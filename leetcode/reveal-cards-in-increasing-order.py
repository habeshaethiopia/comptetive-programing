class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        res=deque()
        deck.sort(reverse=True)
        for i in deck:
            if res:
                x=res.popleft()
                res.append(x)
                res.append(i)
            else:
                res.append(i)
        return list(res)[::-1]

