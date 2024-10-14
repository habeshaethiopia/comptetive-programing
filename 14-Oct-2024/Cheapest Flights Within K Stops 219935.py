# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [float('inf')] * n
        prev[src] = 0
        cnt=-1
        
        # Perform N-1 iterations (where N is the number of nodes)
        limit=False
        for i in range(k+1):
            print(prev[dst])
            curr = prev[:]
            # Relax all edges
            for u, v, w in flights:
                if curr[v]>prev[u]+w:
                    curr[v] =  prev[u]+w   
            prev = curr[:]
        ans=prev[dst]
        print(cnt, prev)
        return -1 if ans==float("inf") else ans
        