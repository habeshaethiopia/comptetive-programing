class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result=0
        n=len(piles)//3
        print(n)
        for i in range(n, len(piles),2):
            result+= piles[i]
        return result
