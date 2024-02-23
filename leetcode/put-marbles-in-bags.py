class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        w=[]
        for i in range(len(weights)-1):
            w.append(weights[i]+weights[i+1])
        w.sort()
        print(w)
        return sum(w[1-k:])-sum(w[:k-1]) if len(weights)>k and k>1 else 0  