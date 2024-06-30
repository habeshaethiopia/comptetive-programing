# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dp(l,r,t):
            
            if l==r:
                return piles[l]
            mx='r'
            if piles[l]> piles[r]:
                mx='l'

            if t==0:
                print(piles[r] if mx=='l' else piles[l])
                return piles[r]+dp(l,r-1,1) if mx=='l' else piles[l]+dp(l+1,r,1)
                
            else:
                return dp(l,r-1,1) if mx=='r' else dp(l+1,r,1)
        alice=dp(0,len(piles)-1,0)
        print(alice)
        return alice<sum(piles)-alice
                 
