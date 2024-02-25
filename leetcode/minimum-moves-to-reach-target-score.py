class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans=0
        while target and maxDoubles:
            if target%2==0 and maxDoubles:
                target/=2
                ans+=1
                maxDoubles-=1
            else:
                target-=1
                ans+=1
        return int(ans +target-1)