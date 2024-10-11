# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        prev = [float('inf')] * (n+1)
        prev[k] = 0
        prev[0]=0
        # Perform N-1 iterations (where N is the number of nodes)
        for i in range(n-1):
            curr = prev[:]
            # Relax all edges
            for u, v, w in times:
                curr[v] = min(curr[v], prev[u]+w)

                # Swap the arrays, prev now points to curr
                prev = curr[:]
        ans=max(prev)
        return -1 if ans==float("inf") else ans
        
