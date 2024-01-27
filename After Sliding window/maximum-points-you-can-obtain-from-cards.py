class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        k=n-k
        x=sum(cardPoints[:k])
        ans=x
        for i in range(k,len(cardPoints)):
            x=x+cardPoints[i]-cardPoints[i-k]
            ans=min(ans,x)
        return sum(cardPoints)-ans