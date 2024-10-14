# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def shortestPath(n: int, src: int):
            prev = [float('inf')] * n
            prev[src] = 0
            # Perform N-1 iterations (where N is the number of nodes)
            for i in range(n-1):
                curr = prev[:]
                # Relax all edges
                for u, v, w in edges:
                    curr[v] = min(curr[v], prev[u]+w)
                    curr[u] = min(curr[u], prev[v]+w)

                # Swap the arrays, prev now points to curr
                if prev== curr:
                    break
                prev = curr[:]
            return prev
        mn=n-1
        ans=n-1
        for i in range(n):
            temp=shortestPath(n,i)
            temp.sort()
            res=bisect_right(temp, distanceThreshold)
            # print(i,temp,res)
            if mn>=res:
                ans=i
                mn=res
        return ans