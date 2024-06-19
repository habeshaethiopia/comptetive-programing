# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
         n,m=len(dungeon), len(dungeon[0])
        
         @lru_cache(None)
         def dfs(x,y):
            if x>=n or y>=m:
                return inf
            if x==n-1 and y==m-1:
                req=-dungeon[x][y]+1
                if req<=0:
                    req=1
                return req
            req=min(dfs(x,y+1),dfs(x+1,y))
            req-=dungeon[x][y]
            if req<=0:
                    req=1
            return req
         return dfs(0,0)
